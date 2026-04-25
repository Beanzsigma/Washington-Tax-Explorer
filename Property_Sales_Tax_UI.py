import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


COUNTY_TAXRATES = {
    "King":       0.0085,
    "Pierce":     0.0092,
    "Snohomish":  0.0080,
    "Spokane":    0.0091,
}
class PropertyTaxFrame(ctk.CTkFrame):
    ctk.set_appearance_mode("dark")
    def __init__(self, parent, controller=None, back_callback=None):
        super().__init__(parent)
        self.controller = controller
        self.back_callback = back_callback

        ctk.CTkLabel(self, text="Washington Property\nTax Calculator", font=("Courier New", 17, "bold")).pack(pady=10)

        ctk.CTkLabel(self, text="Select your county:", font=("Courier New", 16, "bold")).pack(pady=5)
        self.county_var = ctk.StringVar(value="King")
        self.county_dropdown = ctk.CTkOptionMenu(
            self,
            values=list(COUNTY_TAXRATES.keys()),
            variable=self.county_var,
            font=("Courier New", 12),
            text_color="#D25BF0",
            fg_color="#2B2D31",
            button_color="#2B2D31",
            button_hover_color="#635664",
            dropdown_fg_color="#2B2D31",
            dropdown_text_color="#D25BF0",
            dropdown_hover_color="#635664",
        )
        self.county_dropdown.pack(pady=5)

        self.rate_info_label = ctk.CTkLabel(self, text=self._rate_text(), font=("Courier New", 13, "bold"))
        self.rate_info_label.pack(pady=3)
        self.county_var.trace_add("write", lambda *_: self.rate_info_label.configure(text=self._rate_text()))

        ctk.CTkLabel(self, text="Enter property value:", font=("Courier New", 14, "bold")).pack(pady=5)
        self.amount_entry = ctk.CTkEntry(self, font=("Courier New", 12), text_color="#D25BF0")
        self.amount_entry.pack(pady=5)

        ctk.CTkButton(
            self, text="Calculate", font=("Courier New", 14, "bold"),
            border_width=2, border_color="#D25BF0", corner_radius=32,
            text_color="#FFFFFF", fg_color="#2B2D31", hover_color="#635664",
            command=self.calculate,
        ).pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Courier New", 12))
        self.result_label.pack(pady=10)

        ctk.CTkButton(
            self, text="Clear", font=("Courier New", 14, "bold"),
            border_width=2, border_color="#D25BF0", corner_radius=32,
            text_color="#FFFFFF", fg_color="#2B2D31", hover_color="#635664",
            command=self.clear,
        ).pack(pady=5)

        if self.controller:
            ctk.CTkButton(
                self, text="Back to Main", font=("Courier New", 14, "bold"),
                border_width=2, border_color="#D25BF0", text_color="#FFFFFF", fg_color="#2B2D31", hover_color="#635664",
                command=lambda: controller.show_frame("MainDashboard"),
            ).pack(pady=10)
        elif self.back_callback is not None:
            ctk.CTkButton(
                self, text="Back to Main Menu", font=("Courier New", 14, "bold"),
                border_width=2, border_color="#D25BF0",
                text_color="#FFFFFF", fg_color="#2B2D31", hover_color="#635664",
                command=self.back_callback,
            ).pack(pady=10)

    def _rate_text(self):
        rate = COUNTY_TAXRATES[self.county_var.get()]
        return f"Tax rate for {self.county_var.get()} County: {rate:.2%}"

    def parse_currency(self, text: str) -> float:
        cleaned = text.strip().replace(",", "").replace("$", "")
        if not cleaned:
            raise ValueError("Empty amount")
        return float(cleaned)

    def calculate(self):
        try:
            amount = self.parse_currency(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid property value.")
            return

        county = self.county_var.get()
        tax_rate = COUNTY_TAXRATES[county]
        tax_amount = round(amount * tax_rate, 2)
        remaining = round(amount - tax_amount, 2)

        self.result_label.configure(
            text=(
                f"County: {county}\n"
                f"Property value: ${amount:,.2f}\n"
                f"Tax rate: {tax_rate:.2%}\n"
                f"Property tax: ${tax_amount:,.2f}\n"
                f"Remaining after tax: ${remaining:,.2f}"
            )
        )

    def clear(self):
        self.amount_entry.delete(0, tk.END)
        self.county_var.set("King")
        self.result_label.configure(text="")


class PropertyTaxCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Washington Property Tax Calculator")
        self.root.geometry("600x500")
        frame = PropertyTaxFrame(self.root)
        frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = ctk.CTk()
    app = PropertyTaxCalculator(root)
    root.mainloop()