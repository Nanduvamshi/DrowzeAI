# DrowzeAI
DrowzeAI is a real-time driver monitoring system that uses facial emotion recognition, speech emotion analysis, and drowsiness detection based on eye and mouth behavior. It features voice command control and alert systems to enhance driver safety by identifying fatigue, stress, and distraction during driving.

# Features
👁️ Facial Emotion Recognition (DeepFace)

🎤 Speech Emotion Recognition (SER using audio input)

💤 Drowsiness Detection using Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR)

🗣️ Voice Command Interface – Start/Stop monitoring, alerts, and more

⚠️ Alert System with voice feedback and popups

📦 Multi-threaded real-time processing

# Technologies Used
Domain	Libraries / Tools
Computer Vision	OpenCV, Dlib, DeepFace, imutils
Audio Analysis	Librosa, SpeechRecognition, pyttsx3
ML Models	joblib, scikit-learn (for SER model)
TTS / Alerts	pyttsx3, Tkinter, playsound or pygame
Control Logic	Python, threading, queue


 # How to Run
1. 📦 Install Requirements
pip install -r requirements.txt
2. 🧠 Train Speech Emotion Model (Optional)
   python train_ser_model.py
3. 🚀 Start the Monitoring System
   python main.py
# Voice Commands Supported
start monitoring
stop alerts
show stats

# Project Highlights
1. Reduces false positives by using time thresholds for drowsiness/yawning
2. Combines facial + audio emotion for advanced driver awareness
3. Voice-controlled and fully modular
4. Lightweight and deployable on embedded systems

# Future Improvements
1. Integration with GPS/vehicle events
2. Use offline speech models (Vosk) for better voice command performance
3. Cloud-based session analytics

# Developed By
Nandu
