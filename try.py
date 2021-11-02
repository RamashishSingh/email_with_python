import smtplib
from email.message import EmailMessage
import sys
import os
inputs = sys.argv[1]

email = EmailMessage()
email['from'] = 'Ramashish singh'

with open(inputs,'r') as file:
# for i in f.readline():
    
        c = file.readlines()
        email['To'] = c
        email['subject'] = 'hey this is ramashish singh'
        email.set_content('this is ramashihsh sinh just trying how to send email')

with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('singhramashish0502@gmail.com','Bhoomi@05')
    smtp.send_message(email)
