import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import function_processsing
def process_data():
    selected_file = file_label["text"]
    print(selected_file)
    selected_option = dropdown.get()
    print(selected_option)
    function_processsing.slope_UI(selected_file, selected_option)
    # if selected_option =="Calculate Slope":
    #
    #     import arcpy
    #     # outSlope = arcpy.sa.Slope(selected_file, int(result[2]), '"{}"'.format(result[1]), '"{}"'.format(result[0]))
    #     outSlope = arcpy.sa.Slope(selected_file, int(result[2]), '"{}"'.format(result[1]), '"{}"'.format(result[0]))
    #     outSlope.save(e + "slope_output" + b + ".tif")



    # Placeholder code to simulate processing delay
    progress_bar.start(10)

    def finish_processing():
        progress_bar.stop()
        progress_label.config(text="Processing completed!")
        dropdown.focus_set()  # Set focus on the dropdown list

        # Update step flow chart
        step2_label.config(image=checkmark_photo,foreground="#999999",font=("Helvetica", 12, "bold"))
        step3_label.config(image=checkmark_photo,foreground="#999999",font=("Helvetica", 12, "bold"))

        # Display completion message
        messagebox.showinfo("Data Processing", "Data processing completed!")

    window.after(2000, finish_processing)  # Simulate processing delay
#
# # def show_step2():
#     file_frame.pack_forget()  # Hide Step 1 (File Selection)
#     dropdown.pack(pady=10)  # Show Step 2 (Dropdown List)


def browse_KG():
    file_path = filedialog.askopenfilename(filetypes=[("Raster Data", "*.tif")])

    if file_path:
        file_label.config(text=file_path)
        # show_step2()
        progress_label.config(text="File uploaded. Please processing the data.")
        step2_label.config(image=checkmark_photo,foreground="#999999",font=("Helvetica", 12, "bold"))
        step3_label.config(foreground="#000000", font=("Helvetica", 12, "bold"))


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Raster Data", "*.tif")])

    if file_path:
        file_label.config(text=file_path)
        # show_step2()
        progress_label.config(text="File uploaded. Please processing the data.")
        step2_label.config(image=checkmark_photo,foreground="#999999",font=("Helvetica", 12, "bold"))
        step3_label.config(foreground="#000000", font=("Helvetica", 12, "bold"))

def dropdown_changed(event):
    selected_option = dropdown.get()
    if selected_option:
        if selected_option == "Calculate_Slope":
            progress_label.config(text="Please upload a DEM data.")
            progress_label.pack()

        step1_label.config(image=checkmark_photo,foreground="#999999", font=("Helvetica", 12, "bold"))
        step2_label.config(foreground="#000000", font=("Helvetica", 12, "bold"))

window = tk.Tk()
window.title("Geomorphological Landform Classification")
window.geometry("1000x800")

# Styling
window.configure(bg="white")
window.iconbitmap('D:/arcpy_project/Scripts/method/dd.ico')
window.option_add("*Font", "Arial")

# Header
header_frame = tk.Frame(window, bg="#ff9900", height=50)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Classification of Basic Landform Types", font=("Helvetica", 16,"bold"), fg="#ffffff", bg="#ff9900")
header_label.pack(pady=10)

# Step Flow Chart
steps_frame = tk.Frame(window, bg="white")
steps_frame.pack()

circle_image1 = Image.open("D:/arcpy_project/Scripts/method/step1.png")  # Replace with your own circle image
circle_image1 = circle_image1.resize((45, 55))
circle_photo1 = ImageTk.PhotoImage(circle_image1)

circle_image2 = Image.open("D:/arcpy_project/Scripts/method/step2.png")  # Replace with your own circle image
circle_image2 = circle_image2.resize((45, 55))
circle_photo2 = ImageTk.PhotoImage(circle_image2)

circle_image3 = Image.open("D:/arcpy_project/Scripts/method/step3.png")  # Replace with your own circle image
circle_image3 = circle_image3.resize((45, 55))
circle_photo3 = ImageTk.PhotoImage(circle_image3)

checkmark_image = Image.open("D:/arcpy_project/Scripts/method/checkmark.png")  # Replace with your own checkmark image
checkmark_image = checkmark_image.resize((25, 25))
checkmark_photo = ImageTk.PhotoImage(checkmark_image)

step1_label = tk.Label(steps_frame, image=circle_photo1,compound="left",text="Select Application", font=("Helvetica", 12,"bold"), fg="#000000", bg="white")
step1_label.grid(row=0, column=0, padx=10, pady=5)

step2_label = tk.Label(steps_frame, image=circle_photo2,compound="left",text="Select Data", font=("Helvetica", 12,"bold"), fg="#999999", bg="white")
step2_label.grid(row=0, column=1, padx=10, pady=5)

step3_label = tk.Label(steps_frame, image=circle_photo3,compound="left",text="Application Execution", font=("Helvetica", 12,"bold"), fg="#999999", bg="white")
step3_label.grid(row=0, column=2, padx=10, pady=5)

# Dropdown Selection
dropdown_frame = tk.Frame(window, bg="white")
dropdown_frame.pack()

option_label = tk.Label(dropdown_frame, text="Step 1:  Select a region & an Application:", font=("Helvetica", 12,"bold"), bg="#f2f2f2",foreground="dark orange")
option_label.grid(row=0, column=0, padx=10, pady=5)

options = ["Calculate_Slope", "Classify_Plain_and_Mountain"]
dropdown = ttk.Combobox(dropdown_frame, values=options)
dropdown.config(font=("Helvetica", 20))
dropdown.grid(row=0, column=1, padx=10, pady=5)
dropdown.focus_set()
dropdown.bind("<<ComboboxSelected>>", dropdown_changed)


# File Selection
file_frame = tk.Frame(window, bg="white")
file_frame.pack(pady=20)

step11_label = tk.Label(file_frame, text="Step 2: Upload Input Data", font=("Helvetica", 12, "bold"), bg="#f2f2f2",foreground="dark orange")
step11_label.grid(row=0, column=0, padx=10)

file_button = ttk.Button(file_frame, text="Browse",command=browse_file)
file_button.grid(row=0, column=1, padx=10)

file_label = tk.Label(file_frame, text="No File", font=("Helvetica", 12), bg="white")
file_label.grid(row=0, column=2, padx=10)


# dropdown.pack_forget()

# Process Button

process_frame = tk.Frame(window, bg="white")
process_frame.pack(pady=20)

step33_label = tk.Label(process_frame, text="Step 3: Executing Classification", font=("Helvetica", 12, "bold"), bg="#f2f2f2",foreground="dark orange")
step33_label.grid(row=0, column=0, padx=10)

process_button = ttk.Button(process_frame, text="Process Data", command=process_data, style="Accent.TButton")
process_button.grid(row=0, column=1, padx=10)

# Progress Indicator
progress_frame = tk.Frame(window, bg="white")
progress_frame.pack(pady=10)

# if dropdown.get() is "Calculate Slope":
#     progress_label = tk.Label(progress_frame, text="Upload a DEM data to begin.", font=("Helvetica", 12), bg="#f2f2f2")
#     progress_label.pack()

progress_label = tk.Label(progress_frame, text="Please select an application.", font=("Helvetica", 12), bg="#f2f2f2")
progress_label.pack()

style = ttk.Style()
style.theme_use("default")
style.configure("custom.Horizontal.TProgressbar", thickness=20, troughcolor="#e0e0e0", background="#ff9900")

progress_bar = ttk.Progressbar(progress_frame, mode="indeterminate", style="custom.Horizontal.TProgressbar")
progress_bar.pack(pady=5)

window.mainloop()
