
from deepface import DeepFace
import cv2

def detect_facial_emotion():
    cap = cv2.VideoCapture(0)
    print("[INFO] Starting facial emotion recognition. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            dominant_emotion = result[0]['dominant_emotion']
            cv2.putText(frame, f'Emotion: {dominant_emotion}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except Exception as e:
            print("Emotion detection error:", e)
        
        cv2.imshow('Facial Emotion Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
