import yfinance as yf
import pandas as pd
from typing import Optional

def fetch_vix_data(period: str = "7d") -> Optional[pd.DataFrame]:
    """
    Fetch VIX data from Yahoo Finance.

    Args:
        period: Time period for data (e.g., '7d', '1mo', '1y')

    Returns:
        DataFrame with date and vix_close columns, or None if failed
    """
    try:
        # Fetch data with progress disabled for cleaner output
        vix = yf.download("^VIX", period=period, progress=False)

        if vix.empty:
            print("Warning: No VIX data retrieved")
            return None

        # Reset index and handle multi-level columns
        vix = vix.reset_index()
        if isinstance(vix.columns, pd.MultiIndex):
            vix.columns = vix.columns.droplevel(1)

        # Select and rename columns efficiently
        vix = vix[["Date", "Close"]].copy()
        vix.columns = ["date", "vix_close"]

        # Ensure consistent float type for vix_close
        vix["vix_close"] = vix["vix_close"].astype(float)

        # Ensure date is datetime type
        vix["date"] = pd.to_datetime(vix["date"])

        # Sort by date for consistency (defensive programming)
        vix = vix.sort_values("date").reset_index(drop=True)

        return vix

    except Exception as e:
        print(f"Error fetching VIX data: {e}")
        return None

def save_vix_data(vix_data: pd.DataFrame, filename: str = "vix_data.csv") -> bool:
    """
    Save VIX data to CSV file.

    Args:
        vix_data: DataFrame to save
        filename: Output filename

    Returns:
        True if successful, False otherwise
    """
    try:
        vix_data.to_csv(filename, index=False)
        return True
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")
        return False

def latest_vix_value(vix_data: pd.DataFrame) -> float:
    """
    Get the latest (most recent) VIX value from the DataFrame.

    Args:
        vix_data: DataFrame with vix_close column

    Returns:
        Latest VIX close value as float
    """
    return float(vix_data.iloc[-1]["vix_close"])

if __name__ == "__main__":
    # Fetch and save VIX data
    vix_data = fetch_vix_data()

    if vix_data is not None and save_vix_data(vix_data):
        print(f"VIX data saved to vix_data.csv ({len(vix_data)} rows)")
        print(f"Latest VIX value: {latest_vix_value(vix_data):.2f}")
        print("\nRecent VIX data:")
        print(vix_data)  # Show all data instead of just tail
    else:
        print("Failed to fetch or save VIX data")
