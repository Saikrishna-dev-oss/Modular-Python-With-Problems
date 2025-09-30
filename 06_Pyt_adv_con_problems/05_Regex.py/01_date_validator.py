import time as t #to calculate time of Completion
import datetime  #to check Enterd date is Valid or not
import re   
import tkinter as tk   #GUI
from tkinter import messagebox

class Date_validator :
    @staticmethod
    def is_valid_date(date):
        pattern = r'^(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[0-2])-\d{4}$' #checks for corect format only
        return bool(re.match(pattern,date))

def valid_date():
    user_input = date_entry.get()
    if not Date_validator.is_valid_date(user_input) :
        messagebox.showinfo("Result","❌ Incorrect format. Use DD-MM-YYYY.")

    day,month,year = map(int,user_input.split("-")) #Splitting the string into day,moth,yr
    try :
        datetime.date(year,month,day)
        messagebox.showinfo("Result" ,"✅Date is Valid")
    except ValueError as e:
        messagebox.showinfo("Result" ,f"❌Invalid Date {e}")
# GUI preparation code
start = t.time()
root = tk.Tk()
root.title("Date Validator")
root.geometry("500x300")

tk.Label(root,text="Enter the Date").pack(pady=5)
date_entry = tk.Entry(root,width=30)
date_entry.pack(pady=5)

tk.Button(root,text = "Validate",command = valid_date).pack(pady = 5)
root.mainloop()
end = t.time()
print(f"Time Taken for Completion of Program {end-start :.3} seconds")
