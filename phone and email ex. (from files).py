import re
import os
import subprocess
import sys
from datetime import datetime

# Function to check and install required libraries
def check_and_install_libraries():
    required_libraries = ['pandas', 'tkinter']
    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Run library check
check_and_install_libraries()

# Importing libraries after ensuring they're installed
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# Regular expressions for phone numbers and emails
phone_regex = re.compile(r'''
    (\d{3}|\(\d{3}\))?              # area code (optional)
    (\s|-|\.)?                      # separator (optional)
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (optional)
''', re.VERBOSE)

email_regex = re.compile(r'''
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    \.[a-zA-Z]{2,}                  # dot-something (2 or more characters)
''', re.VERBOSE)

# Function to extract phone numbers and emails
def extract_data(text):
    matches = {
        "Phone Numbers": [],
        "Emails": []
    }

    # Find phone numbers
    for groups in phone_regex.findall(text):
        phone_number = '-'.join([groups[0], groups[2], groups[4]])
        matches["Phone Numbers"].append(phone_number)

    # Find email addresses
    matches["Emails"].extend(email_regex.findall(text))

    return matches

# Save extracted data to Excel
def save_to_excel(data):
    # Save location: Directory where the script is stored
    script_directory = os.path.dirname(os.path.abspath(__file__))
    current_date = datetime.now().strftime("%m-%d-%Y")
    default_filename = f"Extracted Data ({current_date}).xlsx"
    output_path = os.path.join(script_directory, default_filename)

    df = pd.DataFrame({
        "Phone Numbers": data["Phone Numbers"],
        "Emails": data["Emails"]
    })
    df.to_excel(output_path, index=False)

    messagebox.showinfo("Success", f"Data saved to {output_path}")

# Function for GUI actions
def run_extraction():
    input_text = text_input.get("1.0", tk.END).strip()  # Get the input text

    if not input_text:
        messagebox.showerror("Error", "Please provide input text or select a file.")
        return

    try:
        # Extract data and save it to the script directory
        extracted_data = extract_data(input_text)
        save_to_excel(extracted_data)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Browse for an input file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, content)

# GUI setup
root = tk.Tk()
root.title("Phone and Email Extractor")

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=10, fill="x")

tk.Label(input_frame, text="Input Text or File:").pack(anchor="w")
text_input = tk.Text(input_frame, height=10, width=50)
text_input.pack(fill="x", padx=5, pady=5)

tk.Button(input_frame, text="Browse File", command=browse_file).pack(pady=5)

# Extract button
tk.Button(root, text="Extract and Save", command=run_extraction, bg="green", fg="white").pack(pady=10)

# Run the GUI loop
root.mainloop()
