import tkinter as tk
from tkinter import messagebox

class TaxCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Washington Tax Calculator")
        self.root.geometry("400x300")

        
        self.tax_rate = 0.065

    
        tk.Label(root, text="Enter amount:").pack(pady=5)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)

       
        tk.Label(root, text="Washington sales tax rate: 6.5%").pack(pady=5)
        self.change_rate_var = tk.BooleanVar()
        tk.Checkbutton(root, text="Change tax rate as a percentage", variable=self.change_rate_var, command=self.toggle_rate_entry).pack(pady=5)

        
        self.rate_entry = tk.Entry(root)
        self.rate_entry.pack(pady=5)
        self.rate_entry.pack_forget()  

        tk.Button(root, text="Calculate", command=self.calculate).pack(pady=10)

    
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

     
        tk.Button(root, text="Clear", command=self.clear).pack(pady=5)

    def toggle_rate_entry(self):
        if self.change_rate_var.get():
            self.rate_entry.pack()
        else:
            self.rate_entry.pack_forget()
            self.rate_entry.delete(0, tk.END)

    def parsecurrency(self, text):
        cleaned = text.strip().replace(',', '').replace('$', '')
        if not cleaned:
            raise ValueError("Empty amount")
        return float(cleaned)

    def parsetaxrate(self, text):
        cleaned = text.strip().replace('%', '').replace(',', '')
        if not cleaned:
            raise ValueError("Empty rate")
        value = float(cleaned)
        return value / 100 if value > 1 else value

    def calculate(self):
        try:
            amount = self.parsecurrency(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount.")
                return

            if self.change_rate_var.get():
                try:
                    new_rate = self.parsetaxrate(self.rate_entry.get())
                    self.tax_rate = new_rate
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid tax rate.")
                    return

            tax = round(amount * self.tax_rate, 2)
            total = round(amount + tax, 2)

            self.result_label.config(text=f"Tax: ${tax:.2f}\nTotal: ${total:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def clear(self):
        self.amount_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.change_rate_var.set(False)
        self.toggle_rate_entry()
        self.result_label.config(text="")
        self.tax_rate = 0.065  

if __name__ == "__main__":
    root = tk.Tk()
    app = TaxCalculator(root)
    root.mainloop()