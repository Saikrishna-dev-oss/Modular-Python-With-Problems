import re
import time as t
import tkinter as tk
from tkinter import messagebox
class Email_utils:
    allowed_domains = ["google.com","yahoo.com",'outlook.com','gcet.edu.in','gmail.com']
    @staticmethod
    def email_validation(email):
        if (email.count('@') !=1  or len(email) < 6):               # structural check
            print("Validation failed : Structure Error")
            return False
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$' #regex for pattern validation
        if not re.match(pattern,email):
            print("Pattern Error")
            return False
        domain = email.split('@')[-1]                               # Domain check
        return domain in Email_utils.allowed_domains
    
def validate_email():
    user_input = email_entry.get()
    if Email_utils.email_validation(user_input):
        messagebox.showinfo("Result","Email is Valid")

    else:
        messagebox.showinfo("Result","Invalid Email")

# Creating a GUI window
start = t.time()
root = tk.Tk()
root.title("Email Validator")
root.geometry("500x300")
# tk.Label(root,text="Enter the Email",pady=5)
tk.Label(root,text="Enter the Email").pack(pady=5)
email_entry = tk.Entry(root, width = 30)
email_entry.pack(pady = 5)

tk.Button(root,text = "validate",command=validate_email).pack(pady=10)
root.mainloop()
end = t.time()
print(f"Time of Execution is : {end-start:.3} Seconds")

