import hashlib
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Replace path and file with path and file you want to monitor for integrity
files_to_monitor = [
    r'c:\users\user\documents\file.txt',
    # Add more file paths as needed
]

# Define your email settings
smtp_server = 'smtp.office365.com'   
smtp_port = 587
smtp_username = 'username@example.com'
smtp_password = 'strongpassword'
sender_email = 'logs@example.com'
receiver_email = 'logs@example.com'

def calculate_md5(file_path):
    """Calculate MD5 hash for a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def send_email(subject, body):
    """Send email notification."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        server.quit()
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def write_to_log(log_message):
    """Write log message to log.txt."""
    with open('log.txt', 'a') as log_file:
        log_file.write(log_message + '\n')

def main():
    # Generate a unique filename based on current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'values_{date_str}.txt'

    # Calculate and store hash values in the file
    with open(filename, 'w') as f:
        for file_path in files_to_monitor:
            hash_value = calculate_md5(file_path)
            f.write(f"{file_path}: {hash_value}\n")

    # Check for changes compared to the previous version
    try:
        with open('previous_values.txt', 'r') as f:
            previous_values = f.read()

        with open(filename, 'r') as f:
            current_values = f.read()

        if current_values != previous_values:
            send_email("File Integrity Alert", "Changes detected in monitored files.")
            write_to_log("File integrity alert sent via email.")
            with open('problemfound.txt', 'w') as problem_file:
                problem_file.write("Changes detected in monitored files.")
    except FileNotFoundError:
        pass

    # Rename the current file to be used as the previous version for the next check
    try:
        import os
        if not os.path.exists('previous_values.txt'):
            os.rename(filename, 'previous_values.txt')
        else:
            os.remove(filename)
    except Exception as e:
        print(f"Error renaming file: {e}")
        write_to_log(f"Error renaming file: {e}")

if __name__ == '__main__':
    main()
