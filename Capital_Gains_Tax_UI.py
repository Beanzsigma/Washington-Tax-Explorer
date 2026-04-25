import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image

class CapitalGainsTaxFrame(ctk.CTkFrame):
    ctk.set_appearance_mode("dark")
    def __init__(self, parent, controller=None, back_callback=None):
        super().__init__(parent)
        self.controller = controller
        self.back_callback = back_callback
        self.tax_rate = 0.07

        ctk.CTkLabel(self, text="Washington Capital\nGains Tax Calculator", font=("Courier New", 20, "bold")).pack(pady=10)
        ctk.CTkLabel(self, text="Enter capital gains amount:", font=("Courier New", 16, "bold")).pack(pady=5)
        self.amount_entry = ctk.CTkEntry(self, font=("Courier New", 12), text_color='#33f875')
        self.amount_entry.pack(pady=5)

        ctk.CTkLabel(self, text="Default capital gains tax rate: 7%\n(No tax applies on gains ≤ $250,000)", font=("Courier New", 14, "bold")).pack(pady=5)
        self.change_rate_var = tk.BooleanVar()
        self.checkbutton = ctk.CTkCheckBox(
            self,
            text="Change tax rate as a percentage", font=("Courier New", 12, "bold"),
            variable=self.change_rate_var,
            command=self.toggle_rate_entry,
        )
        self.checkbutton.pack(pady=5)

        self.rate_entry = ctk.CTkEntry(self, font=("Courier New", 12), text_color='#33f875')

        ctk.CTkButton(self, text="Calculate", font=("Courier New", 14, "bold"), border_width=2, border_color="#33F875", corner_radius=32, text_color="#FFFFFF", fg_color="#2B2D31", hover_color="#3A684E", command=self.calculate).pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Courier New", 12))
        self.result_label.pack(pady=10)

        ctk.CTkButton(self, text="Clear", font=("Courier New", 14, "bold"), command=self.clear, border_width=2, border_color="#33F875", text_color="#FFFFFF", fg_color="#2B2D31", hover_color="#3A684E", corner_radius=32).pack(pady=5)

        if self.controller:
            ctk.CTkButton(
                self,
                text="Back to Main", font=("Courier New", 14, "bold"), border_width=2, border_color="#33F875", text_color="#FFFFFF", hover_color="#3A684E", fg_color="#2B2D31", corner_radius=32,
                command=lambda: controller.show_frame("MainDashboard"),
            ).pack(pady=10)
        elif self.back_callback is not None:
            self.back_button = ctk.CTkButton(
                self,
                text="Back to Main Menu",
                command=self.back_callback,
                font=("Courier New", 14, "bold"),
                border_width=2,
                border_color="#33F875",
                text_color="#FFFFFF",
                fg_color="#2B2D31", hover_color="#3A684E",
            )
            self.back_button.pack(pady=10)

    def toggle_rate_entry(self):
        if self.change_rate_var.get():
            self.rate_entry.pack(pady=5)
        else:
            self.rate_entry.pack_forget()
            self.rate_entry.delete(0, tk.END)

    def parse_currency(self, text: str) -> float:
        cleaned = text.strip().replace(',', '').replace('$', '')
        if not cleaned:
            raise ValueError("Empty amount")
        return float(cleaned)

    def parse_tax_rate(self, text: str) -> float:
        cleaned = text.strip().replace('%', '').replace(',', '')
        if not cleaned:
            raise ValueError("Empty rate")
        value = float(cleaned)
        return value / 100 if value > 1 else value

    def calculate(self):
        try:
            amount = self.parse_currency(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount.")
                return
            if self.change_rate_var.get():
                try:
                    self.tax_rate = self.parse_tax_rate(self.rate_entry.get())
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid tax rate.")
                    return
            tax = 0.0 if amount <= 250000 else round(amount * self.tax_rate, 2)
            remaining = round(amount - tax, 2)
            self.result_label.configure(
                text=(
                    f"Amount: ${amount:,.2f}\n"
                    f"Tax rate: {self.tax_rate:.2%}\n"
                    f"Capital gains tax: ${tax:,.2f}\n"
                    f"Remaining amount after tax: ${remaining:,.2f}"
                )
            )
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def clear(self):
        self.amount_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.change_rate_var.set(False)
        self.toggle_rate_entry()
        self.result_label.configure(text="")
        self.tax_rate = 0.07


if __name__ == "__main__":
    root = ctk.CTk()
    app = CapitalGainsTaxFrame(root)
    app.pack(fill="both", expand=True)
    root.geometry("400x460")
    root.mainloop()