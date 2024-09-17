import tkinter as tk
from tkinter import ttk
import pydirectinput
import threading
import time







class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Anton Clicker")

        self.running = False
        self.input_var = tk.StringVar()
        self.delay_var = tk.DoubleVar(value=1.0)

        self.create_widgets()
        
    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Input Key:").grid(row=0, column=0, sticky=tk.W)
        self.input_entry = ttk.Entry(frame, textvariable=self.input_var, width=30)
        self.input_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Delay (seconds):").grid(row=1, column=0, sticky=tk.W)
        self.delay_entry = ttk.Entry(frame, textvariable=self.delay_var, width=10)
        self.delay_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        self.start_button = ttk.Button(frame, text="Start", command=self.start_clicking)
        self.start_button.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.stop_button = ttk.Button(frame, text="Stop", command=self.stop_clicking)
        self.stop_button.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

    def start_clicking(self):
        self.running = True
        self.start_button['state'] = tk.DISABLED
        self.stop_button['state'] = tk.NORMAL
        input_key = self.input_var.get()
        delay = self.delay_var.get()
        self.click_thread = threading.Thread(target=self.auto_click, args=(input_key, delay))
        self.click_thread.start()

    def stop_clicking(self):
        self.running = False
        self.start_button['state'] = tk.NORMAL
        self.stop_button['state'] = tk.DISABLED
        self.click_thread.join()

    def auto_click(self, input_key, delay):
        while self.running:
            pydirectinput.press(input_key)
            time.sleep(delay)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
