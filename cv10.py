import os
import cv2
import requests
import datetime
import glob
import subprocess
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import threading

API_KEY = "your_api_key"
URL = "https://api.groq.com/openai/v1/chat/completions"
FILE_NAME = f"data_{datetime.datetime.now().strftime('%Y_%m')}.txt"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# ========== ATLAS FUNCTIONS ==========

def speak(text):
    threading.Thread(target=lambda: subprocess.run(['espeak', '-v', 'en', '-s', '150', text])).start()

def read_all_history():
    all_messages = []
    files = sorted(glob.glob("data_*.txt"))
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("[") and "] User: " in line:
                content = line.split("] User: ", 1)[1].strip()
                all_messages.append({"role": "user", "content": content})
            elif line.startswith("[") and "] Atlas: " in line:
                content = line.split("] Atlas: ", 1)[1].strip()
                all_messages.append({"role": "assistant", "content": content})
    return all_messages[-10:]

def ask_atlas(prompt):
    messages = []
    messages.append({
        "role": "user",
        "content": "you are a voice assistant named atlas, be precise, friendly and helpful, do not use sarcasm at all, do not use gen z slang, keep responses short and clear since they will be spoken out loud, always be straightforward and informative"
    })
    messages.append({
        "role": "assistant",
        "content": "Got it! I am Atlas, your helpful and precise assistant. Ready to help, PLAYER6!"
    })
    messages += read_all_history()
    messages.append({"role": "user", "content": prompt})

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": messages,
        "max_tokens": 256
    }

    try:
        response = requests.post(URL, headers=headers, json=payload)
        if response.status_code == 200:
            reply = response.json()['choices'][0]['message']['content']
            return reply
        else:
            return f"API Error {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Connection Error: {e}"

def save_convo(user_msg, atlas_msg):
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        f.write(f"[{timestamp}] User: {user_msg}\n")
        f.write(f"[{timestamp}] Atlas: {atlas_msg}\n")
        f.write("-" * 20 + "\n")

# ========== GUI ==========

class AtlasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Atlas Vision")
        self.root.configure(bg="#1a1a2e")
        self.root.geometry("1024x600")
        self.fullscreen = False

        self.cap = cv2.VideoCapture(0)
        self.running = True

        self.build_gui()
        self.update_camera()

        self.root.bind("<f>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.add_chat("Atlas", "Atlas Vision active. Ready PLAYER6!")
        speak("Atlas Vision active. Ready PLAYER6!")

    def build_gui(self):
        # ---- Left: Camera Feed ----
        self.left_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.camera_label = tk.Label(self.left_frame, bg="#1a1a2e")
        self.camera_label.pack()

        self.people_label = tk.Label(
            self.left_frame,
            text="People: 0",
            font=("Courier", 14, "bold"),
            fg="#00d4ff",
            bg="#1a1a2e"
        )
        self.people_label.pack(pady=5)

        # Camera buttons
        btn_frame = tk.Frame(self.left_frame, bg="#1a1a2e")
        btn_frame.pack(pady=5)

        tk.Button(
            btn_frame, text="Describe Scene",
            command=self.describe_scene,
            bg="#0f3460", fg="white",
            font=("Courier", 11, "bold"),
            relief=tk.FLAT, padx=10, pady=5
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame, text="Count People",
            command=self.count_people,
            bg="#0f3460", fg="white",
            font=("Courier", 11, "bold"),
            relief=tk.FLAT, padx=10, pady=5
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame, text="Fullscreen (F)",
            command=self.toggle_fullscreen,
            bg="#16213e", fg="#00d4ff",
            font=("Courier", 11, "bold"),
            relief=tk.FLAT, padx=10, pady=5
        ).pack(side=tk.LEFT, padx=5)

        # ---- Right: Chat ----
        self.right_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(
            self.right_frame,
            text="ATLAS",
            font=("Courier", 20, "bold"),
            fg="#00d4ff",
            bg="#1a1a2e"
        ).pack()

        tk.Label(
            self.right_frame,
            text="Voice Assistant",
            font=("Courier", 10),
            fg="#888888",
            bg="#1a1a2e"
        ).pack()

        # Chat display
        self.chat_box = scrolledtext.ScrolledText(
            self.right_frame,
            wrap=tk.WORD,
            width=40,
            height=20,
            bg="#16213e",
            fg="white",
            font=("Courier", 10),
            relief=tk.FLAT,
            state=tk.DISABLED
        )
        self.chat_box.pack(fill=tk.BOTH, expand=True, pady=10)

        self.chat_box.tag_config("user", foreground="#00d4ff")
        self.chat_box.tag_config("atlas", foreground="#00ff88")
        self.chat_box.tag_config("system", foreground="#888888")

        # Input area
        input_frame = tk.Frame(self.right_frame, bg="#1a1a2e")
        input_frame.pack(fill=tk.X, pady=5)

        self.input_box = tk.Entry(
            input_frame,
            bg="#16213e",
            fg="white",
            font=("Courier", 11),
            relief=tk.FLAT,
            insertbackground="white"
        )
        self.input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipady=8)
        self.input_box.bind("<Return>", self.send_message)

        tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            bg="#00d4ff",
            fg="#1a1a2e",
            font=("Courier", 11, "bold"),
            relief=tk.FLAT,
            padx=10
        ).pack(side=tk.RIGHT, padx=5)

        # Status bar
        self.status_label = tk.Label(
            self.right_frame,
            text="Ready",
            font=("Courier", 9),
            fg="#888888",
            bg="#1a1a2e"
        )
        self.status_label.pack()

    def add_chat(self, sender, message):
        self.chat_box.config(state=tk.NORMAL)
        timestamp = datetime.datetime.now().strftime("%H:%M")
        if sender == "You":
            self.chat_box.insert(tk.END, f"[{timestamp}] You: ", "user")
            self.chat_box.insert(tk.END, f"{message}\n\n")
        elif sender == "Atlas":
            self.chat_box.insert(tk.END, f"[{timestamp}] Atlas: ", "atlas")
            self.chat_box.insert(tk.END, f"{message}\n\n")
        else:
            self.chat_box.insert(tk.END, f"{message}\n", "system")
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.see(tk.END)

    def set_status(self, text):
        self.status_label.config(text=text)

    def send_message(self, event=None):
        user_input = self.input_box.get().strip()
        if not user_input:
            return
        self.input_box.delete(0, tk.END)
        self.add_chat("You", user_input)
        self.set_status("Atlas is thinking...")
        threading.Thread(target=self.get_reply, args=(user_input,)).start()

    def get_reply(self, prompt):
        reply = ask_atlas(prompt)
        save_convo(prompt, reply)
        self.root.after(0, lambda: self.add_chat("Atlas", reply))
        self.root.after(0, lambda: self.set_status("Ready"))
        speak(reply)

    def describe_scene(self):
        count = self.face_count
        prompt = f"I can see {count} people through the camera. Give a clear and informative description of what might be happening."
        self.add_chat("Atlas", "Analyzing scene...")
        self.set_status("Analyzing...")
        threading.Thread(target=self.get_reply, args=(prompt,)).start()

    def count_people(self):
        count = self.face_count
        prompt = f"There are {count} people visible in the camera right now. Give a helpful response about this."
        self.add_chat("You", f"[Camera] How many people?")
        self.set_status("Counting...")
        threading.Thread(target=self.get_reply, args=(prompt,)).start()

    def update_camera(self):
        if self.running:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                self.face_count = len(faces)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 212, 255), 2)

                self.people_label.config(text=f"People: {self.face_count}")

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (480, 360))
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.camera_label.imgtk = imgtk
                self.camera_label.config(image=imgtk)

            self.root.after(30, self.update_camera)

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

    def exit_fullscreen(self, event=None):
        self.fullscreen = False
        self.root.attributes("-fullscreen", False)

    def on_close(self):
        self.running = False
        self.cap.release()
        self.root.destroy()

# ========== MAIN ==========

if __name__ == "__main__":
    root = tk.Tk()
    app = AtlasApp(root)
    root.mainloop()