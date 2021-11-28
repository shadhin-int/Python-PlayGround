import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

body = '''
Hello, Admin
I am attaching The Sales Files With This Email.
This Year We Got a Wooping 200% Profit One Our Sales.

Regards,
Team Sales
xyz.com
'''

#Sender Email addresses and password
senders_email = 'your_email@gmail.com'
sender_password = 'your_password'
reveiver_email = 'someones_email@gmail.com'

#MIME Setup
message = MIMEMultipart()
message['From'] = senders_email
message['To'] = reveiver_email
message['Subject'] = 'Software Design and Architechture'
message.attach(MIMEText(body, 'plain'))

## File
attach_file_name = 'python_software_design.pdf'
attach_file = open(attach_file_name, 'rb') 
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) 
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)


#SMTP Connection For Sending Email
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(senders_email, sender_password) #login with mail_id and password
text = message.as_string()
session.sendmail(senders_email, reveiver_email, text)
session.quit()
print('Mail Sent')