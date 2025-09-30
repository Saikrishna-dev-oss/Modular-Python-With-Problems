import tkinter as tk
from tkinter import messagebox
import time as t
import random
import string
import secrets

def is_valid_length(length:int) -> None:
    """Check if the provided length is valid for password generation."""
    if(length < 4):
        raise ValueError("Length must be at least 4 to include all characters")

def get_characters_pools() -> dict:
    '''returns a dictionary of all character pools for password generation'''
    return {
            "uppercase" : string.ascii_uppercase,
            "lowercase" : string.ascii_lowercase,
            "symbols" : string.punctuation,
            "digits" : string.digits
    }

def generate_initial_chars(pools: dict) -> list[str]:
    '''Generate initial characters from each character pool to ensure password complexity'''
    return[
            
            secrets.choice(pools["uppercase"]),
            secrets.choice(pools["lowercase"]),
            secrets.choice(pools["digits"]),
            secrets.choice(pools["symbols"]),
    ]
def get_remaining_characters(pools: dict, count:int) -> list[str]:
    '''Generate remaining characters from all pools to fill the password length'''
    all_char = ''.join(pools.values())
    return [secrets.choice(all_char) for i in range(count)]

def shuffle_password(password_list:list[str]) -> list[str]:
    '''Shuffle the password list to ensure randomness'''
    random.SystemRandom().shuffle(password_list)

    return password_list
def generate_password(length):
    is_valid_length(length) 
    pools = get_characters_pools()
    required_characters = generate_initial_chars(pools)
    remaining_characters = get_remaining_characters(pools,length-len(required_characters))
    password_list = required_characters + remaining_characters
    shuffle_pass = shuffle_password(password_list)
    return ''.join(shuffle_pass)

def strength_check(password:str) -> str:
    '''To Check the Strength of the password Generated'''
    score = 0
    length = len(password)

    # Charaacter type check
    if any(c.isupper() for c in password) :score+=1
    if any(c.islower() for c in password) :score+=1
    if any(c.isdigit() for c in password) :score+=1
    if any(c in string.punctuation for c in password) :score+= 1
    if length >=12 : score+=2

    # Entropy Check
    Entropy_size = 0
    if any(c.islower() for c in password) :Entropy_size+=26
    if any(c.isdigit() for c in password) :Entropy_size+=10
    if any(c.isupper() for c in password) :Entropy_size+=26
    if any(c in string.punctuation for c in password) :Entropy_size+= len(string.punctuation)

    Entropy_bits = length * (Entropy_size.bit_length())
    if Entropy_bits >=60 : score +=1

    if score <=2 : return "🔴 Weak"
    if score <=4 : return "🟡 Medium"
    if score <=6 : return"🟩 Strong"
    else : return "🟣 Very Strong"
#GUI Interface
def run_gui() :
    root = tk.Tk()
    root.title("---Password Generator X Strength Checker---")
    root.geometry("400x250")
    root.resizable(False,False)

    #variables
    length_var = tk.StringVar()
    password_var = tk.StringVar()
    strength_var= tk.StringVar()
            
    #Widgets
    tk.Label(root,text= "Enter Password length(min 4) :").pack(pady=5)
    tk.Entry(root,textvariable= length_var).pack()


    def on_generate() :
        try :
            length = int(length_var.get())
            password = generate_password(length)
            strength = strength_check(password)

            password_var.set(password)
            strength_var.set(strength)

            color_map = {
                "🔴 Weak" : "Red",
                "🟡 Medium" :"Orange",
                "🟩 Strong" : "Green",
                "🟣 Very Strong" :"Purple"
            }
            strength_label.config(fg=color_map.get(strength, "black"))
        except ValueError as ve:
            messagebox.showerror("Invalid Input",str(ve))
            password_var.set("")
            strength_var.set("")
    tk.Button(root, text="Generate Password", command=on_generate).pack(pady=10)
    tk.Label(root, text="Generated Password:").pack()
    tk.Label(root, textvariable=password_var, font=("Courier", 12), fg="blue").pack()
    tk.Label(root, text="Strength:").pack(pady=5)
    strength_label = tk.Label(root, textvariable=strength_var, font=("Arial", 12, "bold"))
    strength_label.pack()
    root.mainloop()

if __name__ == "__main__":
    start = t.time()
    run_gui()
    end = t.time()
    print(f"Execution Time is : {end - start :.3} seconds")