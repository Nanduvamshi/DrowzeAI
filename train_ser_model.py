import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestClassifier

def extract_features():
    # Simulate extracted MFCCs for 200 samples with 40 features each
    return np.random.rand(200, 40), np.random.choice(
        ['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised'], 200
    )

X, y = extract_features()

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
os.makedirs("audio", exist_ok=True)
joblib.dump(model, "audio/speech_emotion_model.pkl")
print("✅ Model saved to audio/speech_emotion_model.pkl")
