import tkinter as tk
from tkinter import ttk, messagebox

def show_entry():
    messagebox.showinfo("Entry Value", f"You typed: {entry.get()}")

def show_selected():
    selected = var_radio.get()
    messagebox.showinfo("Radio Selection", f"You selected: {selected}")

def show_check():
    states = [f"{text}: {var.get()}" for text, var in check_vars.items()]
    messagebox.showinfo("Checkbox States", "\n".join(states))

def show_listbox():
    selected = listbox.curselection()
    items = [listbox.get(i) for i in selected]
    messagebox.showinfo("Listbox Selection", ", ".join(items))

def update_scale(val):
    label_scale.config(text=f"Scale: {val}")

def update_spinbox():
    label_spin.config(text=f"Spinbox: {spinbox.get()}")

root = tk.Tk()
root.title("All Tkinter Widgets Demo")
root.geometry("600x700")

# Label
tk.Label(root, text="🔤 Label Widget").pack()

# Entry
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Show Entry", command=show_entry).pack()

# Text
tk.Label(root, text="📝 Text Widget").pack()
text = tk.Text(root, height=4, width=40)
text.pack()

# Button
tk.Button(root, text="Click Me", command=lambda: messagebox.showinfo("Button", "Button clicked!")).pack()

# Checkbuttons
tk.Label(root, text="☑️ Checkbutton Widgets").pack()
check_vars = {}
for option in ["Option A", "Option B", "Option C"]:
    var = tk.BooleanVar()
    check_vars[option] = var
    tk.Checkbutton(root, text=option, variable=var).pack()
tk.Button(root, text="Show Check States", command=show_check).pack()

# Radiobuttons
tk.Label(root, text="🔘 Radiobutton Widgets").pack()
var_radio = tk.StringVar(value="None")
for choice in ["Choice 1", "Choice 2", "Choice 3"]:
    tk.Radiobutton(root, text=choice, variable=var_radio, value=choice).pack()
tk.Button(root, text="Show Radio Selection", command=show_selected).pack()

# Listbox
tk.Label(root, text="📋 Listbox Widget").pack()
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)
listbox.pack()
tk.Button(root, text="Show Listbox Selection", command=show_listbox).pack()

# Canvas
tk.Label(root, text="🎨 Canvas Widget").pack()
canvas = tk.Canvas(root, width=200, height=100, bg="lightblue")
canvas.create_oval(50, 20, 150, 80, fill="green")
canvas.pack()

# Scale
tk.Label(root, text="📏 Scale Widget").pack()
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_scale)
scale.pack()
label_scale = tk.Label(root, text="Scale: 0")
label_scale.pack()

# Spinbox
tk.Label(root, text="🔢 Spinbox Widget").pack()
spinbox = tk.Spinbox(root, from_=1, to=10, command=update_spinbox)
spinbox.pack()
label_spin = tk.Label(root, text="Spinbox: 1")
label_spin.pack()

# Progressbar
tk.Label(root, text="📶 Progressbar Widget").pack()
progress = ttk.Progressbar(root, length=200, mode='determinate')
progress['value'] = 70
progress.pack()

# Menu
def dummy_action():
    messagebox.showinfo("Menu", "Menu item clicked!")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=dummy_action)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()