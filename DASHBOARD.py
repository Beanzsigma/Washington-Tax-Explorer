import customtkinter as ctk
from Capital_Gains_Tax_UI import CapitalGainsTaxFrame
from UI_salestax import SalesTaxFrame
from PIL import Image
from Property_Sales_Tax_UI import PropertyTaxFrame

window = ctk.CTk()
img_3 = Image.open(r"C:\Users\nisha\Downloads\image-removebg-preview (2).png")
img_2 = Image.open(r"C:\Users\nisha\Downloads\image-removebg-preview (1).png")
img = Image.open(r"C:\Users\nisha\Downloads\image-removebg-preview.png")

label_font = ctk.CTkFont(family="Courier New", size=27, weight="bold")
button_font_2 = ctk.CTkFont(family="Courier New", size=14, weight="bold")
button_font = ctk.CTkFont(family="Courier New", size=17, weight="bold") 

def show_main_dashboard():
    for widget in window.winfo_children():
        widget.destroy()
    window.title("Washington Tax Explorer - Main Dashboard")
    title_label = ctk.CTkLabel(window, text="Washington Tax Explorer", font=label_font, text_color="#FFFFFF")
    label_name = ctk.CTkLabel(window, text="Created by: Nishanth Prabhu", font=ctk.CTkFont(family="Courier New", size=13), text_color="#FFFFFF")
    title_label.place(relx=0.5, rely=0.015, anchor="n")
    label_name.place(relx=0.5, rely=0.1, anchor="n")
    button = ctk.CTkButton(window, text="Sales Tax\nCalculator", command=navigate_to_tax_calculator, font=button_font, fg_color="#2B2D31", text_color="white", hover_color="#51648A", border_width=2, border_color="#6CD5E7", corner_radius=32, image=ctk.CTkImage(img, size=(160, 80)), compound="top")
    button.place(relx=0, rely=1, relwidth=0.33, relheight=0.85, anchor="sw")
    button = ctk.CTkButton(window, text="Capital Gains\nTax\nCalculator", command=navigate_to_capital_gains_calculator, font=button_font_2, fg_color="#2B2D31", text_color="white", hover_color="#465F51", border_width=2, border_color="#77EBAB", corner_radius=32, image=ctk.CTkImage(img_2, size=(100, 80)), compound="top")
    button.place(relx=0.5, rely=1, relwidth=0.33, relheight=0.85, anchor="s")
    placeholder = ctk.CTkButton(window, text="Property\nSales Tax", command= navigate_to_property_tax_calculator, font=button_font, fg_color="#2B2d31", hover_color="#A37499", border_width=2, border_color="#D25BF0", corner_radius=32, image=ctk.CTkImage(img_3, size=(100, 80)), compound="top")
    placeholder.place(relx=1, rely=1, relwidth=0.33, relheight=0.85, anchor="se")

def navigate_to_tax_calculator():
    for widget in window.winfo_children():
        widget.destroy()
    SalesTaxFrame(window, back_callback=show_main_dashboard).pack(fill="both", expand=True)
    window.title("Washington Tax Explorer - Sales Tax Calculator")



def navigate_to_property_tax_calculator():
        for widget in window.winfo_children():
            widget.destroy()
        PropertyTaxFrame(window, back_callback=show_main_dashboard).pack(fill="both", expand=True)
        window.title("Washington Tax Explorer - Property Sales Tax Calculator")

def navigate_to_capital_gains_calculator():
    for widget in window.winfo_children():
        widget.destroy()
    CapitalGainsTaxFrame(window, back_callback=show_main_dashboard).pack(fill="both", expand=True)
    window.title("Washington Tax Explorer - Capital Gains Tax Calculator")

show_main_dashboard()
window.geometry("400x460")
window.mainloop()

