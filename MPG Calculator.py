# Jonathan Sonnek
# November 20 2025
# MPG Calculator

import tkinter as tk

class MPG_GUI():
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("MPG Calculator")
        self.root.geometry("400x400")

        # Create Frames
        self.frame1 = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)
        self.frame3 = tk.Frame(self.root)
        self.frame1.pack(pady = 10)
        self.frame2.pack(pady = 10)
        self.frame3.pack(pady = 10)

        # Create result variable and label
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self.root, textvariable=self.result_var)
        self.result_label.pack(pady = 10)

        # Create labels for entry boxes
        tk.Label(self.frame1, text="Enter number of gallons:").pack(side="left")
        tk.Label(self.frame1, text="Enter number of miles:").pack(side="left")

        # Create entry widgets
        self.entry_gallons = tk.Entry(self.frame2)
        self.entry_gallons.pack(side="left")
        self.entry_miles = tk.Entry(self.frame2)
        self.entry_miles.pack(side="left")

        # Create buttons
        self.calculate = tk.Button(self.frame3, text = "calculate", command=self.calculate)
        self.quit_button = tk.Button(self.frame3, text = "quit", command=self.root.destroy)
        self.calculate.pack(side="left")
        self.quit_button.pack(side="left")

    # Calculate MPT
    def calculate(self):
        try:
            gallons = float(self.entry_gallons.get())
            miles = float(self.entry_miles.get())

            MPG = miles/gallons
            self.result_var.set(f"MPG: {MPG:.2f}")
        except ValueError:
            self.result_var.set("Please enter valid numbers.")

if __name__ == "__main__":
    app = MPG_GUI()
    app.root.mainloop()