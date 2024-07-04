from email.message import EmailMessage
import random
import smtplib
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_SENDER=os.getenv("SMTP_SENDER")
SMTP_PASS=os.getenv("SMTP_PASS")


Codes_db={}
after_register_access_token=""

def Send_verification_number(receiver_email):
    try:
        email = EmailMessage()
        email['Subject'] = str(generate_number(receiver_email))
        email['From'] = SMTP_SENDER
        email['To'] = receiver_email
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_SENDER, SMTP_PASS)
            server.send_message(email)
    except Exception as e:
        print(e)

def generate_number(email:str):
    a= random.randint(10000,99999)
    Codes_db[email]=a
    return a
    
    
def verify_code(code:int, email: str):
    print(Codes_db[email])
    if Codes_db[email]== code:
        return True
    else:
        return False
    