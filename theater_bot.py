import requests
from bs4 import BeautifulSoup
import schedule
import time

BOT_TOKEN = "ΤΟ_TOKEN_ΣΟΥ"
CHAT_ID = "7899060721"

url = "https://www.more.com/gr-el/tickets/theater/sosmenos/"


def check_theater():

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.text.lower()

    print("Τσεκάρω θέατρο...")

    if "εξαντλήθηκαν" not in text:

        message = "🎭 ΥΠΑΡΧΟΥΝ εισιτήρια για τον Σωσμένο!"

        telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        requests.post(telegram_url, data=payload)

        print("Στάλθηκε Telegram alert!")

    else:
        print("Δεν υπάρχουν εισιτήρια.")


schedule.every().day.at("12:00").do(check_theater)

print("Το theater bot ξεκίνησε...")

while True:
    schedule.run_pending()
    time.sleep(60)