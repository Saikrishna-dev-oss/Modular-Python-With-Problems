# Save this in a separate file and run it
import os

file_path = "D:\\python\\06_Pyt_adv_con_problems.py\\04_class_static_method.py"  # Replace with your actual filename
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

found = False
for i, char in enumerate(content):
    if not char.isascii():
        print(f"Found non-ASCII character at index {i}: {repr(char)}")
        found = True

if not found:
    print("No non-ASCII characters found. Your file looks clean!")