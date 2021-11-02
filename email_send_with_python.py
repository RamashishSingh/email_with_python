import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Ramashish Singh'
email['to'] = 'sandeepcricket3747@gmail.com'
email['subject'] = 'Hey this is Ramashish Singh'

email.set_content('''i am ramashish singh and i am trying to send message using python
                        try to catch
                         if you can
                         ok byeee..........''')

with smtplib.SMTP(host = 'smtp.gmail.com',port = 587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('annukulhad@gmail.com','passwordhkuch01')
    smtp.send_message(email)
