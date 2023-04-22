import yfinance as yf
from backend import *
import yahoo_fin.stock_info as si
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from datetime import datetime

def send_via_mail(ticker,notification_info,time,price):
    sender_email = "dummyy968@gmail.com"
    receiver_email = str(notification_info)

    subject = "Email from US Stock Price"
    message =  "Hello. This is an email about the Stock Market Price. The price for " + str(ticker) + " is " + str(price) + " which has exceeded your entered threshold price. Date: " + str(time)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:

        server.starttls()
        server.login(sender_email, "mnnykegbmeecklfx")
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)


def send_via_phone(ticker, notification_info, time, price):
    account_sid = "AC0e3531c1cb7e774a554b19db166fb225"
    auth_token = "368b3f60c95169b1d1c42b4043cf6ef3"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Hello. This is an email about the Stock Market Price. The price for " + str(ticker) + " is " + str(price) + " which has exceeded your entered threshold price. Date: " + str(time),
                        from_='+16074007579',
                        to='+977'+notification_info
                    )
    print(message.sid)

    # client = vonage.Client(key="d91f50c0", secret="pO8U74zdQBt799vN")
    # sms = vonage.Sms(client)
    # responseData = sms.send_message(
    #     {
    #         "from": "Vonage APIs",
    #         "to": str(notification_info),
    #         "text": "Hello. This is an email about the Stock Market Price. The price for " + str(ticker) + " is " + str(price) + " which has exceeded your entered threshold price. Date: " + str(time),
    #     }
    # )
    # if responseData["messages"][0]["status"] == "0":
    #     print("Message sent successfully.")
    # else:
    #     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


def send_notification(ticker,notification_type,notification_info,time,price):
    # print()
    if notification_type=="email":
        send_via_mail(ticker,notification_info,time,price)
    elif notification_type=="number":
        send_via_phone(ticker,notification_info,time,price)
    
def get_price(symbol):
    current_price=si.get_live_price(symbol)
    print("***Getting current price****", current_price)
    return current_price

def check_threshold(ticker, threshold,notification_type,notification_info):
    price = get_price(ticker)
    if price >= threshold:
        time = datetime.now()
        print(time)
        send_notification(ticker,notification_type,notification_info,time,price)
    else:
        pass


def monitor(entry_id, entered_data):
    print(entered_data)
    symbol = entered_data['symbol']
    threshold = entered_data['threshold']
    notification_type = entered_data['notification']
    time_period = entered_data['time']
    notification_info = entered_data['notification_info']

    if time_period =='1h':
        set_timer = 60
    elif time_period == '1d':
        set_timer = 86400
    elif time_period == '1wk':
        set_timer = 604800
    elif time_period == '1mo':
        set_timer = 2592000

    while True:
        check_threshold(symbol, int(threshold), notification_type, notification_info)
        time_to_wait = set_timer - (time.time() % set_timer)
        time.sleep(time_to_wait)

