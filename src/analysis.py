import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emotion_results.csv")

# Sort by fear score for clarity
df = df.sort_values(by="fear_score", ascending=False)

plt.figure(figsize=(10,5))
plt.bar(df["image"], df["fear_score"])
plt.xticks(rotation=45)
plt.ylabel("Fear Score")
plt.xlabel("Image")
plt.title("Fear Score Across Financial Media Images")
plt.tight_layout()

# Save the plot instead of showing it
plt.savefig("fear_score_analysis.png")
print("Plot saved as fear_score_analysis.png")

print("\nFear Score Summary:")
print(df["fear_score"].describe())
