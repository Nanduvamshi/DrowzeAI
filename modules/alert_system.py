
import pygame
import threading
import tkinter as tk

ALERT_SOUND = "modules/beep.mp3"

def play_alert_sound():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(ALERT_SOUND)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"[ERROR] Failed to play sound: {e}")

def show_popup(message="⚠️ ALERT: Take Action!"):
    def popup():
        root = tk.Tk()
        root.title("Alert")
        root.geometry("300x100")
        label = tk.Label(root, text=message, fg="red", font=("Helvetica", 14, "bold"))
        label.pack(pady=20)
        root.after(3000, root.destroy)
        root.mainloop()
    threading.Thread(target=popup).start()

def trigger_alert(message="⚠️ Attention Required!"):
    threading.Thread(target=play_alert_sound).start()
    show_popup(message)
