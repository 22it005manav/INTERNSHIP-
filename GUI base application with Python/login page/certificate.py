from PIL import Image, ImageDraw, ImageFont
import os
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox

def generate_certificate_and_send_email(output_path='C:\\Users\\DELL\\OneDrive\\New folder\\OneDrive\\Desktop\\login page'):
    with open("email.txt", "r") as file:
        emails = file.read()
    
    with open("username.txt", "r") as file:
        name = file.read()

    with open("event.txt", "r") as file:
        events = file.read()

    # Assuming 'arial.ttf' is in the current working directory, adjust the path if needed
    font_path = os.path.join(os.getcwd(), 'arial.ttf')
    font = ImageFont.truetype(font_path, 60)

    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    
    draw.text(xy=(700, 695), text='Name: {}'.format(name), fill=(0, 0, 0), font=font)
    draw.text(xy=(1070, 695), text='  and  Event: {}'.format(events), fill=(0, 0, 0), font=font)

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Save the certificate with a unique name
    certificate_filename = '{}.jpg'.format(name)
    certificate_path = os.path.join(output_path, certificate_filename)
    img.save(certificate_path)

    # Store in MySQL database
    # Send email with the certificate as an attachment
    sender_email = 'manavbagthaliya2525@gmail.com'
    sender_password = 'xlvr nika zxex ovnp'
    
    subject = 'Certificate for {}'.format(name)
    body = 'Dear {},\n\nAttached is your certificate.\n\nRegards,\nYour Organization'.format(name)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = emails
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(certificate_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= {}".format(certificate_filename))
    msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, emails, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    finally:
        # Close the attachment file
        attachment.close()

        # Delete the file from the folder after storing in the database and sending email
        os.remove(certificate_path)

# # Test the function
# generate_certificate_and_send_email()
