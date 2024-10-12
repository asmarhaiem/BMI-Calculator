import tkinter as tk
from tkinter import messagebox


def save_bmi_data(weight, height, bmi, classification):
    try:
        with open("bmi_data.txt", "a") as f:
            f.write(f"Weight: {weight}, Height: {height}, BMI: {bmi:.2f}, Classification: {classification}\n")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)

        classification = classify_bmi(bmi)

        messagebox.showinfo("Result", f"Your BMI is: {bmi:.2f}\nClassification: {classification}")

        save_bmi_data(weight, height, bmi, classification)


    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Welcome to the BMI Calculator!", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Enter your weight (in kg):").grid(row=1, column=0, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

tk.Label(root, text="Enter your height (in meters):").grid(row=2, column=0, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()
