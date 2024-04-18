import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.png")])

    if file_path:
        file_label.config(text=file_path)
        # show_step2()

# def show_step2():
#     file_frame.pack_forget()  # Hide Step 1 (File Selection)
#     dropdown.pack(pady=10)  # Show Step 2 (Dropdown List)
#     process_button.pack(pady=20)  # Show Step 3 (Process Data)

def process_data():
    selected_option = dropdown.get()

    # Process data based on the selected option
    # ...
    # Display the result or perform additional operations
    result_label.config(text="Data processed successfully!")

window = tk.Tk()
window.title("Step-by-Step Interface")

# Step 1: File Selection
file_frame = tk.Frame(window, bg="#f2f2f2")
file_frame.pack(pady=20)

file_button = ttk.Button(file_frame, text="Browse", command=browse_file)
file_button.grid(row=0, column=0, padx=10)

file_label = tk.Label(file_frame, text="No file selected", font=("Helvetica", 12), bg="#f2f2f2")
file_label.grid(row=0, column=1, padx=10)

# Step 2: Select from Drop-down List (Initially hidden)
options = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar()
dropdown = ttk.Combobox(window, values=options, state="readonly", textvariable=selected_option)

# Step 3: Process Data (Initially hidden)
process_button = ttk.Button(window, text="Process Data", command=process_data)

# Result
result_label = tk.Label(window, text="Result:")

window.mainloop()
