import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['From'] = 'Ramashish singh'
email['to'] = 'sandeepcricket3747@gmail.com'
email['subject'] = 'best Wishes to have a good time in college'

email.set_content(html.substitute({'name':'Ram'}),'html')

with smtplib.SMTP(host = 'smtp.gmail.com',port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('annukulhad@gmail.com','passwordhkuch01')
    smtp.send_message(email)