# Jonathan Sonnek
# November 20 2025
# Automotive Calculator

import tkinter as tk

class AutomotiveCalculatorGUI():
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("Automotive Calculator")
        self.root.geometry("400x400")

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2.pack()

        # Create result variable and label
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self.root, textvariable=self.result_var)
        self.result_label.pack(pady=10)

        # Create checkbox variables
        self.oil_var = tk.IntVar()
        self.lube_var = tk.IntVar()
        self.radiator_var = tk.IntVar()
        self.trans_var = tk.IntVar()
        self.inspect_var = tk.IntVar()
        self.muffler_var = tk.IntVar()
        self.tire_var = tk.IntVar()

        # Create checkboxes
        tk.Checkbutton(self.frame1, text="Oil Change ($30)", variable=self.oil_var).pack(anchor="w")
        tk.Checkbutton(self.frame1, text="Lube Job ($20)", variable=self.lube_var).pack(anchor="w")
        tk.Checkbutton(self.frame1, text="Radiator Flush ($40)", variable=self.radiator_var).pack(anchor="w")
        tk.Checkbutton(self.frame1, text="Transmission Fluid ($100)", variable=self.trans_var).pack(anchor="w")
        tk.Checkbutton(self.frame1, text="Inspection ($35)", variable=self.inspect_var).pack(anchor="w")
        tk.Checkbutton(self.frame1, text="Muffler Replacement ($200)", variable=self.muffler_var).pack(anchor="w")
        tk.Checkbutton(self.frame1, text="Tire Rotation ($20)", variable=self.tire_var).pack(anchor="w")

        # Create buttons
        self.calculate = tk.Button(self.frame2, text="calculate", command=self.calculate)
        self.quit_button = tk.Button(self.frame2, text="quit", command=self.root.destroy)
        self.calculate.pack(side="left")
        self.quit_button.pack(side="left")

    # Create calculate function
    def calculate(self):
            total = 0
            if self.oil_var.get() == 1:
                total += 30
            if self.lube_var.get() == 1:
                total += 20
            if self.radiator_var.get() == 1:
                total += 40
            if self.trans_var.get() == 1:
                total += 100
            if self.inspect_var.get() == 1:
                total += 35
            if self.muffler_var.get() == 1:
                total += 200
            if self.tire_var.get() == 1:
                total += 20
            self.result_var.set(f"Cost: {total:.2f}")

if __name__ == "__main__":
    automotive_calculator = AutomotiveCalculatorGUI()
    automotive_calculator.root.mainloop()
