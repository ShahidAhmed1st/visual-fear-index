from deepface import DeepFace
import cv2
import os

IMAGE_PATH = "data/images/img1.jpg"

if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError("Image not found. Put test.jpg in data/images/")

img = cv2.imread(IMAGE_PATH)

result = DeepFace.analyze(
    img,
    actions=["emotion"],
    enforce_detection=False
)

emotion_scores = result[0]["emotion"]
dominant_emotion = result[0]["dominant_emotion"]

print("Detected emotions:")
for emotion, score in emotion_scores.items():
    print(f"{emotion}: {round(score, 2)}")

print(f"\nDominant emotion: {dominant_emotion}")
fear_score = (
    emotion_scores["fear"]
    + emotion_scores["angry"]
    + emotion_scores["sad"]
    + emotion_scores["surprise"]
)
print(f"\nFear Score: {round(float(fear_score), 2)}")
