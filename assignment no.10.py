import tkinter as tk
from tkinter import messagebox

# Function to classify blood pressure
def classify_blood_pressure():
    try:
        # Get values from the user input
        systolic = int(entry_systolic.get())
        diastolic = int(entry_diastolic.get())

        # Blood pressure classification
        if systolic < 120 and diastolic < 80:
            classification = "Normal"
        elif 120 <= systolic <= 129 and diastolic < 80:
            classification = "Elevated"
        elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
            classification = "High Blood Pressure (Hypertension Stage 1)"
        elif 140 <= systolic <= 179 or 90 <= diastolic <= 119:
            classification = "High Blood Pressure (Hypertension Stage 2)"
        elif systolic >= 180 or diastolic >= 120:
            classification = "Hypertensive Crisis (Consult your doctor immediately)"
        else:
            classification = "Invalid Blood Pressure Values"

        # Display result in a message box
        messagebox.showinfo("Blood Pressure Classification", f"Your classification: {classification}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for blood pressure.")

# Create the main window (GUI)
root = tk.Tk()
root.title("Blood Pressure Classification App")
root.geometry("300x200")

# Create labels and entry fields for systolic and diastolic pressure
label_systolic = tk.Label(root, text="Enter Systolic Pressure (Top number):")
label_systolic.pack(pady=5)
entry_systolic = tk.Entry(root)
entry_systolic.pack(pady=5)

label_diastolic = tk.Label(root, text="Enter Diastolic Pressure (Bottom number):")
label_diastolic.pack(pady=5)
entry_diastolic = tk.Entry(root)
entry_diastolic.pack(pady=5)

# Create a button to classify blood pressure
classify_button = tk.Button(root, text="Classify Blood Pressure", command=classify_blood_pressure)
classify_button.pack(pady=20)

# Run the application
root.mainloop()


