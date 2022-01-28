import smtplib
from smtplib import SMTPException
import requests
import json


# ertha api url
BASE_URL = f'https://api.ertha.com/mainnet/tokens/'

# gmail account credentials to be used
# it is a good idea to create a dummy account just for this

GMAIL_USER = 'ertha@gmail.com'
GMAIL_PASS = 'YourSecurePasswordHere'
  
HEADERS = {
    "content-type": "application/json"
}

# example: MONITORED_HEX = f'{BASE_URL}123456'
MONITORED_HEX = f'{BASE_URL}<hex number>'

# HTTP GET request
MONITORED_HEX_REQ = requests.get(f'{MONITORED_HEX}', headers=HEADERS).json()

# simple condition
if MONITORED_HEX_REQ['is_reserved'] == False:
    #pirnt("Buy now now now!!!"
    sent_from = GMAIL_USER
    
    # To yourself
    to = ['ertha@gmail.com']
    
    # Your desired subject
    subject = 'Open to buy now on ertha io'
    
    # This will be the body of the email so it may be good idea to include a link to the hex for faster response
    body = 'Hey dude your tile is now available... https://globe.ertha.com#123456'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        
        #print('Email sent!')
    except SMTPException as e:
        print(e)
else:
  print("Unknown error occurred") 
