from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import Client
import requests
import re


# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

def get_prices():
    r = requests.get("https://google.com/search?q=bitcoin+price",stream=True)
    data = r.text
    priceIndex = re.search(r'\b(1 Bitcoin)\b',data)
    price = data[priceIndex.start()+12:priceIndex.start()+20]
    print(price)

    client = Client(account_sid, auth_token)

    if(price<'13000'):
        message = client.messages.create(
            #phone number to send to
            to="",
            #phone number given by twilio
            from_="",
            body="Buy coins! 1 Bitcoin = "+price)
    elif(price>'20000'):
        message = client.messages.create(
            #phone number to send to
            to="",
            #phone number given by twilio
            from_="",
            body="Sell coins! 1 Bitcoin = "+price)

scheduler = BlockingScheduler()
scheduler.add_job(get_prices, 'interval', hours=1)
scheduler.start()
