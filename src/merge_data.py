import pandas as pd
from datetime import datetime, timezone
from typing import Optional

try:
    # Try relative import (when run as module)
    from .market_data import fetch_vix_data
except ImportError:
    # Try absolute import (when run as script)
    from market_data import fetch_vix_data

def merge_emotion_and_vix_data(
    emotion_csv: str = "emotion_results.csv",
    vix_period: str = "7d",
    output_csv: str = "final_dataset.csv"
) -> Optional[pd.DataFrame]:
    """
    Merge emotion analysis data with VIX market data.

    Args:
        emotion_csv: Path to emotion analysis CSV file
        vix_period: Time period for VIX data (e.g., '7d', '1mo')
        output_csv: Output CSV filename

    Returns:
        Merged DataFrame or None if failed
    """
    try:
        # Load emotion analysis data
        print(f"Reading emotion results from {emotion_csv}...")
        emotion_df = pd.read_csv(emotion_csv)
        print(f"Loaded {len(emotion_df)} emotion analysis records")

        # Schema validation
        required_cols = {"fear_score", "image"}
        missing = required_cols - set(emotion_df.columns)
        if missing:
            raise ValueError(f"Missing required columns in {emotion_csv}: {missing}")

        # Fetch VIX data
        print(f"Fetching VIX data for period: {vix_period}...")
        vix_df = fetch_vix_data(period=vix_period)

        if vix_df is None:
            print("Error: Could not fetch VIX data")
            return None

        # Get latest VIX value
        latest_vix = float(vix_df.iloc[-1]["vix_close"])
        print(f"Latest VIX value: {latest_vix:.2f}")

        # Add VIX data to emotion DataFrame
        emotion_df["vix_close"] = round(latest_vix, 2)

        # Add correlation placeholder (fear score vs VIX gap)
        emotion_df["fear_vix_gap"] = emotion_df["fear_score"] - emotion_df["vix_close"]

        # Add analysis timestamp (UTC for consistency)
        analysis_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        emotion_df["analysis_timestamp"] = analysis_date

        # Save merged dataset
        print(f"Saving merged dataset to {output_csv}...")
        emotion_df.to_csv(output_csv, index=False)

        print(f"✅ Successfully created {output_csv} with {len(emotion_df)} records")
        return emotion_df

    except FileNotFoundError:
        print(f"Error: Could not find file {emotion_csv}")
        return None
    except Exception as e:
        print(f"Error merging data: {e}")
        return None

if __name__ == "__main__":
    # Merge emotion and VIX data
    merged_df = merge_emotion_and_vix_data()

    if merged_df is not None:
        print("\n📊 Sample of merged dataset:")
        print(merged_df.head())
        print(f"\n📈 VIX-Fear Score Correlation Summary:")
        print(f"Average Fear Score: {merged_df['fear_score'].mean():.2f}")
        print(f"Current VIX: {merged_df['vix_close'].iloc[0]:.2f}")
    else:
        print("❌ Failed to create merged dataset")
