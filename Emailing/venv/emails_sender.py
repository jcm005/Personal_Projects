
import smtplib # creates smtp server communicates the language od the email
from email.message import EmailMessage
from string import Template #allows $ to substitute dollars signs into text
from pathlib import Path

html = Template(Path('index.html').read_text())


email = EmailMessage()

email['from'] = 'Joseph Mattern'
email['to'] = 'joseph.mattern@stonybrook.edu'
email['subject'] = 'You send this from a python program'


email.set_content(html.substitute({'name' :'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # hello im awakw message
    smtp.starttls() # encryption mechanism
    smtp.login('matternjoseph0505@gmail.com', 'Standby1')    #connect to the email account
    smtp.send_message(email)
    print('all good boss!')