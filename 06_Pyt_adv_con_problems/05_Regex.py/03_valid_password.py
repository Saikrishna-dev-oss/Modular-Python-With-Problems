import re
import tkinter as tk
from tkinter import messagebox
import time as t
class Pass_validator:
    @staticmethod
    def is_valid_pass(pas,min_len = 8):
        if(len(pas) >= 8) :
            pattern = r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()]).{'+str(min_len)+',}$'
            return bool(re.match(pattern,pas))
def valid_pass():
    user_input = pass_Entry.get()
    if Pass_validator.is_valid_pass(user_input):
        messagebox.showinfo("Reslut","Valid Password")
    else:
        messagebox.showinfo("Result","InValid Pasword")

# GUI
start = t.time()
root = tk.Tk()
root.title("🔑---Welcome To Password Validator---🔑")
root.geometry("500x300")

tk.Label(root,text="Enter the Password").pack(pady=5)
pass_Entry = tk.Entry(root,width=30)
pass_Entry.pack(pady=5)

tk.Button(root,text="validate",command=valid_pass).pack(pady=5)
root.mainloop()
end = t.time()
print(f"Time Taken for Completion of Program {end-start :.3} seconds")