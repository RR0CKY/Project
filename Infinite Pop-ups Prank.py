import winsound  # Sound play karne ke liye (Windows built-in)
import random
import time
import tkinter as tk

root = tk.Tk()
root.withdraw()

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

# Fast 5 real-looking popups
for i in range(5):
    # Beep sound play karna (Error sound feel ke liye)
    winsound.MessageBeep(winsound.MB_ICONHAND)

    popup = tk.Toplevel(root)
    popup.title("Windows Security - Critical Alert")

    # Window ka exact size
    win_w, win_h = 450, 220

    # Random position
    pos_x = random.randint(50, max(50, screen_w - win_w - 50))
    pos_y = random.randint(50, max(50, screen_h - win_h - 50))

    popup.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
    popup.attributes("-topmost", True)  # Screen ke upar rahega
    popup.configure(bg="#f0f0f0")  # Windows style light gray background

    # Red Top Header Bar
    header = tk.Frame(popup, bg="#d9534f", height=35)
    header.pack(fill="x")

    title_label = tk.Label(
        header,
        text="⚠️ SYSTEM THREAT DETECTED",
        font=("Segoe UI", 11, "bold"),
        fg="white",
        bg="#d9534f",
    )
    title_label.pack(pady=5)

    # Message Content
    body_frame = tk.Frame(popup, bg="#f0f0f0")
    body_frame.pack(expand=True, fill="both", padx=20, pady=10)

    msg_label = tk.Label(
        body_frame,
        text=f"Trojan.Win32.Generic #{i+1}\nYour personal files might be compromised!",
        font=("Segoe UI", 10),
        fg="#333333",
        bg="#f0f0f0",
        justify="left",
    )
    msg_label.pack(anchor="w", pady=10)

    # OK Button
    btn = tk.Button(
        popup,
        text="Remove Threat Now",
        font=("Segoe UI", 10, "bold"),
        bg="#0078d4",
        fg="white",
        activebackground="#005a9e",
        activeforeground="white",
        bd=0,
        padx=15,
        pady=5,
        command=popup.destroy,
    )
    btn.pack(pady=(0, 15))

    root.update()
    time.sleep(0.4)

root.mainloop()