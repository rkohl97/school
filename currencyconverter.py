from tkinter import Tk, ttk
from tkinter import *
import requests
import json
from PIL import Image, ImageTk

# Colors
cor0 = "#FFFFFF"  # white
cor1 = "#333333"  # black
cor2 = "#EB5D51"  # red
cor3 = "#808080"  # grey
cor4 = "#00FF00"  # green

root = Tk()
root.geometry('300x320')
root.title('Currency Converter')
root.configure(bg=cor4)  # Changes background color to green
root.resizable(height=FALSE, width=FALSE)

# Frames
top = Frame(root, width=300, height=60, bg=cor2) # Changes background color to red
top.grid(row=0, column=0)

main = Frame(root, width=300, height=260, bg=cor4) # Changes background color to green
main.grid(row=1, column=0)

def convert(): # uses currency converter api to convert 
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    if not amount:
        result['text'] = "Please enter an amount"
        return

    try:
        float(amount)
    except ValueError:
        result['text'] = "Invalid amount"
        return

    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'INR':
        symbol = '₹'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'BRL':
        symbol = 'R$'
    elif currency_2 == 'CAD':
        symbol = 'CA $'
    elif currency_2 == 'JPY': #added jpn currency
        symbol = '¥'
    elif currency_2 == 'KRW':# added korean won
        symbol = '₩'
    else:
        symbol = ''

    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "8613bff65amsh32d222c825619cep116c9ajsn828c4cade693"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    if "result" in data and "convertedAmount" in data["result"]:
        converted_amount = data["result"]["convertedAmount"]
        formatted = symbol + " {:,.2f}".format(converted_amount)
        result['text'] = formatted
        print(converted_amount, formatted)
    else:
        result['text'] = "Conversion error"

# Top frame
icon = Image.open('icon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=5, padx=13, pady=30, anchor=CENTER, font=('Arial', 16, 'bold'), bg=cor2, fg=cor0)
app_name.grid(row=0, column=0)  # Use grid instead of place

# Main frame
result = Label(main, text=" ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Arial', 15, 'bold'), bg=cor0, fg=cor1)
result.place(x=50, y=10)

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD', 'JPY', 'KRW'] #added jpn and korean currency

from_label = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Arial', 10, 'bold'), bg=cor0, fg=cor1)
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Arial", 12, 'bold'))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Arial', 10, 'bold'), bg=cor0, fg=cor1)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Arial", 12, 'bold'))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Arial", 12, 'bold'), relief=SOLID)
value.place(x=50, y=155)

button = Button(main, text="Convert", width=19, padx=5, height=1, bg=cor3, fg=cor0, font=("Arial", 12, 'bold'), command=convert)
button.place(x=50, y=210)

root.mainloop()
