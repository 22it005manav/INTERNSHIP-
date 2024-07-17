import smtplib
import random

def generate_otp():
    # Generate a 6-digit OTP
    return str(random.randint(100000, 999999))

def send_otp(email, otp):
    # Your Gmail account credentials
    gmail_user = 'dharmkasundra284@gmail.com'  # Replace with your Gmail email
    gmail_password = 'bkxs ghob fhxn vmtj'  # Replace with your Gmail password

    # SMTP server and port for Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create the email message
    subject = 'Your OTP for Verification'
    body = f'Your OTP is: {otp}'
    message = f'Subject: {subject}\n\n{body}'

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)

        # Send the email
        server.sendmail(gmail_user, email, message)

        # Close the connection
        server.quit()

        print('OTP sent successfully!')
    except Exception as e:
        print(f'Error sending OTP: {e}')

# Example usage
email_address = 'kasundradharm2845@gmail.com'  # Replace with the recipient's email address
otp_code = generate_otp()
send_otp(email_address, otp_code)
