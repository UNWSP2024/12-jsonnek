# Jonathan Sonnek
# November 20 2025
# Call Cost Calculator

# A long-distance provider charges the following rates for telephone calls:
#
# Rate Category	Rate per Minute
# Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
# Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
# Off-Peak (midnight through 5:59 P.M.) 	$0.05
#
# Write a GUI application that allows the user to select a rate category
# (from a set of radio buttons), and enter the number of minutes of the call into an Entry widget.
# An info dialog box  should display the charge for the call.

import tkinter as tk
from tkinter import messagebox

class CallCalculatorGUI():
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("Long Distance Call Calculator")
        self.root.geometry("400x400")

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)
        self.frame3 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        # Create radio button variable
        self.rate_var = tk.StringVar()
        self.rate_var.set("day")

        # Create radio buttons
        tk.Radiobutton(self.frame1, text="Daytime (6am–5:59pm)   $0.02/min",
                       variable=self.rate_var, value="day").pack(anchor="w")

        tk.Radiobutton(self.frame1, text="Evening (6pm–11:59pm)  $0.12/min",
                       variable=self.rate_var, value="evening").pack(anchor="w")

        tk.Radiobutton(self.frame1, text="Off-Peak (midnight–5:59am)  $0.05/min",
                       variable=self.rate_var, value="offpeak").pack(anchor="w")

        # Create entry widget
        tk.Label(self.frame1, text="Time (min):").pack(side="left")
        self.entry_time = tk.Entry(self.frame2)
        self.entry_time.pack()

        # Create buttons
        self.calculate_button = tk.Button(self.frame3, text="Calculate", command=self.calculate)
        self.calculate_button.pack(side="left")
        self.quit_button = tk.Button(self.frame3, text="Quit", command=self.root.destroy)
        self.quit_button.pack(side="left")

    # Create calculate function
    def calculate(self):
        rate = self.rate_var.get()
        if rate == "day":
            cost_per_min = 0.02
        elif rate == "evening":
            cost_per_min = 0.12
        else:
            cost_per_min = 0.05

        try:
            time = float(self.entry_time.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number of minutes.")
            return

        cost = cost_per_min * time
        messagebox.showinfo("Call Charge", f"Charge for call: ${cost:.2f}")

if __name__ == "__main__":
    calculator = CallCalculatorGUI()
    calculator.root.mainloop()
