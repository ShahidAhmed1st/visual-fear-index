# 📉 Visual Fear Index

**Visual Fear Index** is a computer vision–driven project that analyzes emotional signals in financial media images and compares them with real-world market volatility using the VIX index.

The goal is to explore whether **visual fear amplification in media** aligns with **actual market fear**.

---

## 🔍 Project Overview

Financial markets are influenced not only by numbers, but also by **human emotion, perception, and narrative**.

This project:
- Detects emotions in financial media images using **DeepFace**
- Quantifies a **Fear Score** from detected emotions
- Fetches real-time **VIX (Volatility Index)** data from Yahoo Finance
- Merges emotional data with market volatility
- Visualizes insights using a **Streamlit dashboard**

---

## 🧠 Core Questions Explored

- Do fear-heavy visuals correlate with market volatility?
- Is media-driven fear exaggerated compared to actual market conditions?
- Can emotion analysis offer alternative insights into market sentiment?

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **DeepFace**
- **Pandas**
- **Matplotlib**
- **yFinance**
- **Streamlit**
- **Git & GitHub**

---

## 📁 Project Structure

```
visual-fear-index/
│
├── app.py                     # Streamlit dashboard
├── src/
│   ├── emotion_detector.py    # Single image emotion analysis
│   ├── batch_emotion_analysis.py
│   ├── market_data.py         # VIX data fetcher
│   ├── merge_data.py          # Emotion + VIX merger
│   └── analysis.py            # Fear score visualization
│
├── data/
│   └── images/                # Financial media images
│
├── emotion_results.csv
├── final_dataset.csv
├── fear_score_analysis.png
├── vix_data.csv
├── .gitignore
└── README.md
```

## ⚙️ How It Works

1. **Emotion Detection**
   - Uses DeepFace to extract emotion probabilities from images
   - Emotions analyzed: fear, anger, sadness, surprise, neutral, etc.

2. **Fear Score Construction**
   - Aggregates fear-related emotions
   - Serves as a proxy for emotional intensity in visuals

3. **Market Context**
   - Fetches the VIX index as a measure of market uncertainty
   - Adds market volatility context to each image analysis

4. **Visualization**
   - Streamlit dashboard displays:
     - Emotion analysis dataset
     - Fear score per image
     - Current VIX value
     - Interpretation notes

---

## 🚀 Running the Project Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

**Run the Streamlit app:**

```bash
streamlit run app.py
```

**Open in browser:**

```
http://localhost:8501
```