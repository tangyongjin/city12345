import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Email configuration
smtp_server = 'mail.sinnet.com.cn'
smtp_port = 25  # This is the default port for TLS encryption
sender_email = 'tyj@sinnet.com.cn'
sender_password = '@Xiaoke_2023'
receiver_email = 'tyj@sinnet.com.cn'
subject = 'Test111'

# Create the email content
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Email body
body = 'This is the body of your email.'
message.attach(MIMEText(body, 'plain'))


# Establish an SMTP connection and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use TLS for encryption
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print('Email sent successfully!')
except Exception as e:
    print('Error: ', e)
