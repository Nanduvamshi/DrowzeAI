
import threading
from modules import facial_emotion, speech_emotion, voice_commands, alert_system
from modules.Detection import start_drowsiness_detection


def start_facial_monitoring():
    facial_emotion.detect_facial_emotion()

def start_speech_monitoring():
    emotion = speech_emotion.predict_emotion()
    if emotion in ['angry', 'sad']:
        alert_system.trigger_alert(f"Detected {emotion} tone in speech!")

def voice_command_listener():
    while True:
        command = voice_commands.listen_command()
        voice_commands.handle_command(command)

def main():
    print("AI Monitor System Starting...\n")
    threading.Thread(target=start_facial_monitoring).start()
    threading.Thread(target=start_speech_monitoring).start()
    threading.Thread(target=voice_command_listener).start()
    threading.Thread(target=start_drowsiness_detection, daemon=True).start()

if __name__ == "__main__":
    main()
