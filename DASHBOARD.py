import customtkinter as ctk
from UI_salestax import SalesTaxFrame
from PIL import Image

window = ctk.CTk()
img = Image.open(r"C:\Users\nisha\Downloads\image-removebg-preview.png")

label_font = ctk.CTkFont(family="Courier New", size=27, weight="bold")

button_font = ctk.CTkFont(family="Courier New", size=16, weight="bold") 

def show_main_dashboard():
    for widget in window.winfo_children():
        widget.destroy()
    window.title("Washington Tax Explorer - Main Dashboard")
    title_label = ctk.CTkLabel(window, text="Washington Tax Explorer", font=label_font, text_color="#6CD5E7")
    title_label.place(relx=0.5, rely=0.05, anchor="n")
    button = ctk.CTkButton(window, text="Go to\nSales Tax\nCalculator", command=navigate_to_tax_calculator, font=button_font, fg_color="#2B2D31", text_color="white", hover_color="#3C3F45", border_width=2, border_color="#6CD5E7", corner_radius=32, image=ctk.CTkImage(img, size=(160, 80)), compound="top")
    button.place(relx=0, rely=1, relwidth=0.33, relheight=0.85, anchor="sw")

def navigate_to_tax_calculator():
    for widget in window.winfo_children():
        widget.destroy()
    SalesTaxFrame(window, back_callback=show_main_dashboard).pack(fill="both", expand=True)
    window.title("Washington Tax Explorer - Sales Tax Calculator")

show_main_dashboard()
window.geometry("400x430")
window.mainloop()

