import logging
logging.debug("Tihs is debug message")


# Set the minimum logging level to INFO,
logging.basicConfig(level=logging.INFO,force=True)

# Get a logger object
log = logging.getLogger(__name__)
logging.debug("Tihs is debug message")



# Start the log file
log.info("Hello world")

import csv
try:
    with open("C:\\Users\\keerthivasan.a\\OneDrive - Protiviti Member Firm\\Desktop\\Sprint 38.xlsx","r") as text:
     out=csv.reader(text)   
except FileNotFoundError as ex:
    print("File not found:" +str(ex))

x=5
if x>5:
   raise ValueError("It should be greater than 5")
print(x)

from email.message import EmailMessage
message = EmailMessage()
print(message)
sender = "me@example.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient
print(message)
From: me@example.com
To: you@example.com
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
print(message)

From: me@example.com
To: you@example.com
Subject: Greetings from me@example.com to you@example.com!
body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)