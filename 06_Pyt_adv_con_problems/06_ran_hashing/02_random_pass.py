import tkinter as tk
from tkinter import messagebox
import time as t
import random, string, secrets

# --- Backend Functions  ---
def is_valid_length(length: int) -> None:
    if length < 4:
        raise ValueError("Length must be at least 4 to include all characters")

def get_characters_pools() -> dict:
    return {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "symbols": string.punctuation,
        "digits": string.digits
    }

def generate_initial_chars(pools: dict) -> list[str]:
    return [
        secrets.choice(pools["uppercase"]),
        secrets.choice(pools["lowercase"]),
        secrets.choice(pools["digits"]),
        secrets.choice(pools["symbols"]),
    ]

def get_remaining_characters(pools: dict, count: int) -> list[str]:
    all_char = ''.join(pools.values())
    return [secrets.choice(all_char) for _ in range(count)]

def shuffle_password(password_list: list[str]) -> list[str]:
    random.SystemRandom().shuffle(password_list)
    return password_list

def generate_password(length: int) -> str:
    is_valid_length(length)
    pools = get_characters_pools()
    required = generate_initial_chars(pools)
    remaining = get_remaining_characters(pools, length - len(required))
    password_list = required + remaining
    return ''.join(shuffle_password(password_list))

def strength_check(password: str) -> str:
    score = 0
    length = len(password)

    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if length >= 12: score += 2

    entropy_size = 0
    if any(c.islower() for c in password): entropy_size += 26
    if any(c.isdigit() for c in password): entropy_size += 10
    if any(c.isupper() for c in password): entropy_size += 26
    if any(c in string.punctuation for c in password): entropy_size += len(string.punctuation)

    entropy_bits = length * (entropy_size.bit_length())
    if entropy_bits >= 60: score += 1

    if score <= 2: return "🔴 Weak"
    if score <= 4: return "🟡 Medium"
    if score <= 6: return "🟩 Strong"
    else: return "🟣 Very Strong"

# --- GUI Class ---
class PasswordApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("---Password Generator X Strength Checker---")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # Variables
        self.length_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.strength_var = tk.StringVar()

        # Widgets
        tk.Label(self.root, text="Enter Password length (min 4):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.length_var).pack()

        tk.Button(self.root, text="Generate Password", command=self.on_generate).pack(pady=10)

        tk.Label(self.root, text="Generated Password:").pack()
        tk.Label(self.root, textvariable=self.password_var, font=("Courier", 12), fg="blue").pack()

        tk.Label(self.root, text="Strength:").pack(pady=5)
        self.strength_label = tk.Label(self.root, textvariable=self.strength_var, font=("Arial", 12, "bold"))
        self.strength_label.pack()

    def on_generate(self):
        try:
            length = int(self.length_var.get())
            password = generate_password(length)
            strength = strength_check(password)

            self.password_var.set(password)
            self.strength_var.set(strength)

            color_map = {
                "🔴 Weak": "red",
                "🟡 Medium": "orange",
                "🟩 Strong": "green",
                "🟣 Very Strong": "purple"
            }
            self.strength_label.config(fg=color_map.get(strength, "black"))
        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))
            self.password_var.set("")
            self.strength_var.set("")

    def run(self):
        self.root.mainloop()

# --- Entry Point ---
if __name__ == "__main__":
    start = t.time()
    app = PasswordApp()
    app.run()
    end = t.time()
    print(f"Execution Time is: {end - start:.3f} seconds")