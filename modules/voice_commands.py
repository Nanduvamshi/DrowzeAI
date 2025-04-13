
import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("[VOICE] Listening for command...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print(f"[VOICE] You said: {command}")
        return command
    except sr.UnknownValueError:
        print("[VOICE] Could not understand audio")
    except sr.RequestError:
        print("[VOICE] Could not request results")
    
    return ""

def handle_command(command):
    if "start monitoring" in command:
        print("[ACTION] Starting monitoring...")
    elif "stop alerts" in command:
        print("[ACTION] Stopping alerts...")
    elif "show stats" in command:
        print("[ACTION] Showing system stats...")
    else:
        print("[VOICE] Command not recognized.")

