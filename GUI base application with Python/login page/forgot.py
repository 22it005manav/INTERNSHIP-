from tkinter import *
from tkinter import messagebox
import pymysql
import smtplib
import otpgen

otpss = otpgen.generate_otps
def send_otp(email, otpss):
    # Your Gmail account credentials
    gmail_user = 'manavbagthaliya2525@gmail.com'  # Replace with your Gmail email
    gmail_password = 'xlvr nika zxex ovnp'  # Replace with your Gmail password

    # SMTP server and port for Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create the email message
    subject = 'Your OTP for Verification'
    body = f'Your OTP is: {otpss}'
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

def next():
    email_address=wm1.get()
    if wm1.get() == "":
        messagebox.showerror("Empty", "Please enter your E-mail")
    else:
        try:
            con = pymysql.connect(host="localhost", user='root', password='2525', database='userdata')
            mycursor = con.cursor()

            query = 'select * from data where email=%s'
            mycursor.execute(query, (wm1.get()))
            row = mycursor.fetchone()

            if row is not None:
                otp_code_veri = otpss
                email_address = wm1.get()

                send_otp(email_address, otp_code_veri)
                messagebox.showinfo("Success", "OTP sent successfully! Check your email. ")
                # messagebox.showinfo(otpss)
                login_window.destroy()  # Destroy the window here, not in otp_verification.py
                import otp
            else:
                messagebox.showerror("Error", "E-mail does not exist.")
                
        except pymysql.Error as e:
            print(f"Database error: {e}")
            messagebox.showerror("Error", "Database error occurred.")
        finally:
            mycursor.close()
            con.close()

# Tkinter GUI
login_window = Tk()
login_window.title("Login Page")
login_window.configure(bg="black")
window_width = 400
window_height = 300
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
login_window.resizable(False, False)

frame_right = Frame(login_window, bg="black")
frame_right.pack(side=RIGHT, padx=20, pady=10)

heading = Label(frame_right, text=" FORGOT PASSWORD ", font=('Microsoft Yaei UI Light', '23', 'bold'), bg="black", fg="white")
heading.grid(row=0, column=0, columnspan=2, pady=(10, 10))

wm = Label(frame_right, text="E-Mail: ", font=('Open Sans', 9), fg='white', bg='black')
wm.grid(row=1, column=0, sticky='w', padx=25, pady=21)
wm1 = Entry(frame_right, font=('Microsoft Yaei UI Light', 11), width=28, bd=0, fg="white", bg="firebrick1")
wm1.grid(row=1, column=0, padx=80, pady=10)

logbt = Button(frame_right, text=' Next ', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', activebackground='firebrick1', cursor='hand2', bd=6, width=17, command=next)
logbt.grid(row=3, column=0, padx=30, pady=20)

login_window.mainloop()
