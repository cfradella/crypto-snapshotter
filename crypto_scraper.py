#  NOTE: Coinmarketcap API recently migrated to a newer, more secure public api
#  that requires a key and proper auth setup. The API endpoints listed below
#  are sadly deprecated :-(

import requests
import smtplib
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root,height=500,width=700 ,bg="#282929")
canvas.pack()

frame = tk.Frame(root,bg="#4e5461")

frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

def price_check():
    #  Bitcoin API call
    btc_endpoint = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    btc_req = requests.get(btc_endpoint)
    btc_price = "$" + str(btc_req.json()[0]['price_usd'][0:7])
    print(btc_price)

    #  Litecoin API call
    ltc_endpoint = "https://api.coinmarketcap.com/v1/ticker/litecoin/"
    ltc_req = requests.get(ltc_endpoint)
    ltc_price = "$" + str(ltc_req.json()[0]['price_usd'][0:5])

    #  Ethereum API call
    eth_endpoint = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
    eth_req = requests.get(eth_endpoint)
    eth_price = "$" + str(eth_req.json()[0]['price_usd'][0:6])

    return f"spoop"

price_label = tk.Label(frame,text=price_check(),fg= "#e8e8e8",bg="#4e5461",font=("Helvetica", 26))
price_label.pack()

# def configger():
#     price_label.config(text=price_check())

refresh_button = tk.Button(frame,text="Refresh",padx=10, pady=5,fg="black",bg="#4e5461")

refresh_button.pack()

def email_sender(data):
    user_email = "cfradella@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)  #  An SMTP encapsulating an SMTP connection. Params - host, port
    server.ehlo()  #  Identify ourselves to an ESMTP server.
    server.starttls()  #  Puting the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
    server.ehlo()  #  Do it again!

    server.login(user_email, "zfzjjhbmdukjtonj")  #  Log in on an SMTP server that requires authentication
    subject = "Your cryptocurrency daily snapshot"
    body = f"Heres are the coins you follow: {data}"

    message = "Subject: {subject} \n\n {body}"

    server.sendmail(  #  Sending an email. Params - Sender, Reciever, Body
        user_email,
        user_email,
        message
    )

    server.quit() #  Terminate the SMTP session and close the connection

email_sender(price_check)
root.mainloop()
