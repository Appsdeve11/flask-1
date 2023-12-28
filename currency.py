from tkinter import Tk, Label, Entry, Button, messagebox
from forex_python.converter import CurrencyRates, CurrencyCodes

def convert_currency():
    # Get user inputs
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    amount = amount_entry.get()

    # Validate currency codes
    currency_codes = CurrencyCodes()
    if not currency_codes.get_currency_name(from_currency) or not currency_codes.get_currency_name(to_currency):
        messagebox.showerror("Invalid Currency Code", "Please enter valid currency codes.")
        return

    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid number for the amount.")
        return

   
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)

    result_label.config(text=f"Converted Amount: {round(converted_amount, 2)} {to_currency}")

window = Tk()
window.title("Currency Converter")

from_currency_label = Label(window, text="From Currency:")
from_currency_label.grid(row=0, column=0, padx=5, pady=5)
from_currency_entry = Entry(window)
from_currency_entry.grid(row=0, column=1, padx=5, pady=5)

to_currency_label = Label(window, text="To Currency:")
to_currency_label.grid(row=1, column=0, padx=5, pady=5)
to_currency_entry = Entry(window)
to_currency_entry.grid(row=1, column=1, padx=5, pady=5)

amount_label = Label(window, text="Amount:")
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = Entry(window)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

convert_button = Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = Label(window)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()