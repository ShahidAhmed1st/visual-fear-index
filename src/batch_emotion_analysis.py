import os
import cv2
import pandas as pd
from deepface import DeepFace

IMAGE_DIR = "data/images"

records = []

print(f"Processing images in {IMAGE_DIR}...")

for file in os.listdir(IMAGE_DIR):
    if not file.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    print(f"Processing {file}...")
    path = os.path.join(IMAGE_DIR, file)
    img = cv2.imread(path)

    if img is None:
        print(f"Failed to load {file}")
        continue

    try:
        result = DeepFace.analyze(
            img,
            actions=["emotion"],
            enforce_detection=False
        )

        emotions = result[0]["emotion"]
        dominant = result[0]["dominant_emotion"]

        fear_score = (
            emotions["fear"]
            + emotions["angry"]
            + emotions["sad"]
            + emotions["surprise"]
        )

        records.append({
            "image": file,
            "dominant_emotion": dominant,
            "fear_score": round(float(fear_score), 2),
            **{k: round(float(v), 2) for k, v in emotions.items()}
        })

    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Processed {len(records)} images.")

df = pd.DataFrame(records)
df.to_csv("emotion_results.csv", index=False)

print("Batch analysis complete.")
print(df)
