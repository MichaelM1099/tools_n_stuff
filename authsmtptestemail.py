import smtplib
from email.mime.text import MIMEText

def send_email(smtp_server, port, username, password, to_address, subject, body):
    try:
        # Create a MIMEText object with email body
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = to_address

        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)

        # Send email
        server.sendmail(username, to_address, msg.as_string())

        # Disconnect 
        server.quit()

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# input for SMTP server, port, username, and password
smtp_server = input("Enter SMTP server: ")
port = int(input("Enter port: "))
username = input("Enter your email address: ")
password = input("Enter your email password: ")
to_address = input("Enter recipient email address: ")
subject = input("Enter email subject: ")
body = input("Enter email body: ")

result = send_email(smtp_server, port, username, password, to_address, subject, body)

if result:
    print("Email sent successfully.")
else:
    print("Failed to send email. Please check your credentials and try again.")
