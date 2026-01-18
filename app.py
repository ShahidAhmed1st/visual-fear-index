import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Visual Fear Index", layout="wide")

st.title("📉 Visual Fear Index Dashboard")

st.write("App started")

if not os.path.exists("final_dataset.csv"):
    st.error("❌ final_dataset.csv not found. Run merge script first.")
    st.stop()

df = pd.read_csv("final_dataset.csv")

st.write("Dataset loaded:", df.shape)

st.subheader("📊 Emotion Analysis Dataset")
st.dataframe(df)

st.subheader("🔥 Fear Score per Image")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df["image"], df["fear_score"])
ax.set_ylabel("Fear Score")
ax.set_xlabel("Image")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.subheader("📈 Market Volatility Context")
st.metric(
    label="Current VIX Value",
    value=df["vix_close"].iloc[0]
)

st.subheader("🧠 Interpretation")
st.write(
    """
    - Fear Score quantifies emotional exaggeration in financial media visuals.
    - VIX represents market-wide volatility and uncertainty.
    - This dashboard compares visual media fear with market volatility.
    """
)

