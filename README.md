# DrowzeAI
DrowzeAI is a real-time driver monitoring system that uses facial emotion recognition, speech emotion analysis, and drowsiness detection based on eye and mouth behavior. It features voice command control and alert systems to enhance driver safety by identifying fatigue, stress, and distraction during driving.
🧠 Features
👁️ Facial Emotion Recognition (DeepFace)

🎤 Speech Emotion Recognition (SER using audio input)

💤 Drowsiness Detection using Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR)

🗣️ Voice Command Interface – Start/Stop monitoring, alerts, and more

⚠️ Alert System with voice feedback and popups

📦 Multi-threaded real-time processing

🔧 Technologies Used
Domain	Libraries / Tools
Computer Vision	OpenCV, Dlib, DeepFace, imutils
Audio Analysis	Librosa, SpeechRecognition, pyttsx3
ML Models	joblib, scikit-learn (for SER model)
TTS / Alerts	pyttsx3, Tkinter, playsound or pygame
Control Logic	Python, threading, queue
📁 Folder Structure
bash
Copy
Edit
DriveGuard-AI/
├── audio/                          # Trained SER model and recorded clips
│   └── speech_emotion_model.pkl
├── modules/                        # Modularized feature logic
│   ├── Detection.py                # Drowsiness detection logic
│   ├── EAR.py / MAR.py            # Eye/Mouth aspect ratio calculators
│   ├── facial_emotion.py          # DeepFace-based emotion detection
│   ├── speech_emotion.py          # Audio-based SER
│   ├── voice_commands.py          # Voice control logic
│   └── alert_system.py            # Alert popups + TTS
├── main.py                         # Main launcher (multithreaded)
├── shape_predictor_68_face_landmarks.dat
├── train_ser_model.py             # Train your own speech emotion model
├── requirements.txt
└── README.md
▶️ How to Run
1. 📦 Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
2. 🧠 Train Speech Emotion Model (Optional)
bash
Copy
Edit
python train_ser_model.py
3. 🚀 Start the Monitoring System
bash
Copy
Edit
python main.py
🎤 Voice Commands Supported
start monitoring

stop alerts

show stats

📌 Project Highlights
Reduces false positives by using time thresholds for drowsiness/yawning

Combines facial + audio emotion for advanced driver awareness

Voice-controlled and fully modular

Lightweight and deployable on embedded systems

🚀 Future Improvements
Integration with GPS/vehicle events

Use offline speech models (Vosk) for better voice command performance

Cloud-based session analytics

🧑‍💻 Developed By
Nandu
