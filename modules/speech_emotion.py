
import librosa
import numpy as np
import joblib
import sounddevice as sd
import scipy.io.wavfile as wav

MODEL_PATH = "audio/speech_emotion_model.pkl"
model = joblib.load(MODEL_PATH)

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=3, offset=0.5)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def record_audio(filename="audio/recorded.wav", duration=4, fs=44100):
    print("[INFO] Recording audio...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, audio)
    return filename

def predict_emotion():
    audio_file = record_audio()
    features = extract_features(audio_file)
    features = features.reshape(1, -1)
    prediction = model.predict(features)[0]
    print(f"[RESULT] Detected speech emotion: {prediction}")
    return prediction
