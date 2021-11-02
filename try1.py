# import smtplib
# from email.message import EmailMessage
# import sys
# import os
# inputs = sys.argv[1]

# email = EmailMessage()
# email['from'] = 'Ramashish singh'

# with open(inputs,'r') as file:
#     l = file.readline()
# # for i in f.readline():
#     while l != "":
#         for i in file.readlines():
#             email['To'] = i
#             print(email['To'])
#             email['subject'] = 'hey this is ramashish singh'
#             email.set_content('this is ramashihsh sinh just trying how to send email')

#             with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
#                 smtp.set_debuglevel(1)
#                 smtp.ehlo()
#                 smtp.starttls()
#                 smtp.login('singhramashish0502@gmail.com','Bhoomi@05')
#                 smtp.send_message(email)
#                 l = file.readline()

# import smtplib
# from email.message import EmailMessage

# def send_email(TOADDRS):

#     FROMADDR = "singhramashish0502@gmail.com"
#     LOGIN    = FROMADDR
#     PASSWORD = "Bhoomi@05"
#     SUBJECT  = "Welcome to Stack Overflow"

#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.set_debuglevel(1)
#     server.ehlo()
#     server.starttls()
#     server.login(LOGIN, PASSWORD)

#     msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"% (FROMADDR,TOADDRS, SUBJECT) )
#     msg += """ This a test \r\n"""

#     server.sendmail(FROMADDR, TOADDRS, msg)
#     server.quit()
# if __name__ == 'main':
#     f= open("list.txt","r")
#     line_a=f.readline()
#     print(line_a)
#     while line_a !="":
#         send_email(line_a)
#         line_a = f.readline()
#     f.close()



import smtplib
from email.mime.text import MIMEText


def send_email(TOADDRS):    
    FROMADDR = "singhramashish0502@gmail.com"
    LOGIN    = FROMADDR
    PASSWORD = "Bhoomi@05"
    SUBJECT  = "Welcome to Stack Overflow"
    BODY = "Test body"


    msg = MIMEText(BODY)
    msg['Subject'] = SUBJECT
    msg['From'] = 'singhramashish0502@gmail.com'
    msg['To'] = TOADDRS
    send = smtplib.SMTP('smtp.gmail.com',587)
    send.set_debuglevel(1)
    send.ehlo()
    send.starttls() 
    send.login(LOGIN, PASSWORD)
    send.sendmail(msg['From'], msg['To'], msg.as_string())
    send.quit()
with open ("list.txt", "r") as myfile:
    linea = myfile.readline()
    while linea !="":
        data=myfile.readline().replace('\n', '')
        send_email(data)