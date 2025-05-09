import requests
import hashlib
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
import os

# Configuration
URL = "https://www.ticketmaster.fr/fr/manifestation/bad-bunny-billet/idmanif/622243" # URL to watch
HASH_FILE = "site_hash.txt" # Output hash file of website, used to detect changes

##### SMTP Configuration #####
SMTP_SERVER = ""
SMTP_PORT = 587
SMTP_USERNAME = ""
SMTP_PASSWORD = ""
EMAIL_TO = ""
EMAIL_FROM = SMTP_USERNAME

def fetch_site_content():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def get_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def send_email_notification():
    msg = EmailMessage()
    msg.set_content(f"The content of the website {URL} has changed.")
    msg['Subject'] = "🎟️ Changes detected on website"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)

def main():
    content = fetch_site_content()
    current_hash = get_hash(content)

    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            previous_hash = f.read()
        if current_hash != previous_hash:
            send_email_notification()
            with open(HASH_FILE, 'w') as f:
                f.write(current_hash)
    else:
        with open(HASH_FILE, 'w') as f:
            f.write(current_hash)

if __name__ == "__main__":
    main()