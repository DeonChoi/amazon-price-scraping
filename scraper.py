import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
URL = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"}



def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(class_="priceView-hero-price priceView-customer-price").span.get_text().strip('$')
    
    price = float(price)
    print(price)

    if (price < 500):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(os.getenv('USERNAME'), os.getenv('PASSWORD'))

    subject="The price of this item has fallen."
    body = "Check the amazon link" + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        os.getenv('USERNAME'),
        os.getenv('USERNAME'),
        msg
    )
    print('Email sent!')

    server.quit()


check_price()