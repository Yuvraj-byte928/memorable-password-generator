import tkinter as tk
from tkinter import messagebox
import random

def generate_password():
    account = entry_account.get().strip().replace(" ", "").capitalize()
    word    = entry_word.get().strip().replace(" ", "").capitalize()
    number  = entry_number.get().strip()
    feeling = entry_feeling.get().strip().capitalize()

    if not all([account, word, number, feeling]):
        messagebox.showwarning("Oops!", "Please answer all the questions!")
        return

    symbols = {
        "Happy":     "@",
        "Excited":   "!",
        "Love":      "<3",
        "Cool":      "#",
        "Motivated": "*",
        "Calm":      "~",
    }
    symbol = symbols.get(feeling, "!")

    # Clean no-space templates
    templates = [
        f"ILove{word}On{account}{number}",
        f"My{account}Is{word}{number}",
        f"{word}Makes{feeling}{symbol}{number}",
        f"{feeling}About{word}{account}{number}",
        f"{account}For{word}{symbol}{number}",
        f"{account}{word}IsLife{symbol}{number}",
        f"{feeling}With{word}{account}{number}",
        f"{word}IsMyfav{symbol}{account}{number}",
        f"Using{account}Feels{feeling}{symbol}{number}",
        f"{word}On{account}Always{symbol}{number}",
    ]

    password = random.choice(templates)
    result_var.set(password)

def copy_password():
    if not result_var.get():
        return
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied!", "Password copied to clipboard! 📋")

# --- Window ---
root = tk.Tk()
root.title("🔐 Memorable Password Generator")
root.geometry("500x540")
root.configure(bg="#0f0f1a")
result_var = tk.StringVar()

LABEL_STYLE = {"bg": "#0f0f1a", "fg": "#eaeaea", "font": ("Georgia", 11)}
ENTRY_STYLE = {"bg": "#16213e", "fg": "#4ecca3", "font": ("Courier", 12),
               "insertbackground": "white", "relief": "flat", "width": 32}

# --- Title ---
tk.Label(root, text="🔐 Password Maker", bg="#0f0f1a",
         fg="#e94560", font=("Georgia", 20, "bold")).pack(pady=(20, 4))
tk.Label(root, text="Passwords you can actually remember 😄",
         bg="#0f0f1a", fg="#888aaa", font=("Georgia", 9)).pack(pady=(0, 20))

# --- Questions ---
questions = [
    ("📱 What is this account for? (e.g. Instagram)", "account"),
    ("💖 A word you love? (e.g. Reels)", "word"),
    ("🔢 Your lucky number?", "number"),
    ("😊 Feeling? (Happy/Excited/Love/Cool/Motivated/Calm)", "feeling"),
]

entries = {}
for question, key in questions:
    tk.Label(root, text=question, **LABEL_STYLE).pack(anchor="w", padx=40)
    e = tk.Entry(root, **ENTRY_STYLE)
    e.pack(pady=(2, 12), padx=40)
    entries[key] = e

entry_account = entries["account"]
entry_word    = entries["word"]
entry_number  = entries["number"]
entry_feeling = entries["feeling"]

# --- Generate Button ---
tk.Button(root, text="✨ Generate My Password", command=generate_password,
          bg="#e94560", fg="white", font=("Georgia", 11, "bold"),
          relief="flat", padx=12, pady=7).pack(pady=(8, 14))

# --- Result ---
tk.Label(root, text="Your Password:", bg="#0f0f1a",
         fg="#888aaa", font=("Georgia", 9)).pack()
tk.Label(root, textvariable=result_var, bg="#0f0f1a",
         fg="#4ecca3", font=("Courier", 15, "bold")).pack(pady=6)

# --- Copy Button ---
tk.Button(root, text="📋 Copy to Clipboard", command=copy_password,
          bg="#0f3460", fg="white", font=("Georgia", 10),
          relief="flat", padx=8, pady=5).pack(pady=4)

# --- Tip ---
tk.Label(root, text="💡 Keep hitting Generate to find the one that clicks for you!",
         bg="#0f0f1a", fg="#888aaa", font=("Georgia", 8)).pack(pady=(20, 0))

root.mainloop()