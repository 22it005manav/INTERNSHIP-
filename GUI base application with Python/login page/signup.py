from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image, ImageTk
import re
import smtplib

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def checkm(email):
    
    if(re.fullmatch(regex, email)):
        try:
            con = pymysql.connect(host="localhost", user='root', password='2525')
            mycursor = con.cursor()

            query = 'create database if not exists userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table if not exists data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20) )'
            mycursor.execute(query)

        except Exception as e:
            messagebox.showerror('Error', f'Database Connectivity Issue: {str(e)}')
            return

        query = 'select * from data where username=%s'
        mycursor.execute(query, (un1.get()))
        row = mycursor.fetchone()

        if row is not None:
            messagebox.showerror("Error", "Username Already exists")
        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (wm1.get(), un1.get(), ps1.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "account created successfully.")
            email_address = wm1.get()

            send_ml(email_address)
            open_login_page() # Call the function to open the login page

    else:
        messagebox.showerror("Error", "Invalid E-mail")

def send_ml(email):
    # Your Gmail account credentials
    gmail_user = 'manavbagthaliya2525@gmail.com'  # Replace with your Gmail email
    gmail_password = 'xlvr nika zxex ovnp'  # Replace with your Gmail password

    # SMTP server and port for Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create the email message
    subject = 'Successfully  registered.'
    body = f'Thank  you for registering.'
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
    except Exception as e:
        print(f'Error : {e}')
def clear():
    wm1.delete(0, END)
    un1.delete(0, END)
    ps1.delete(0, END)
    fps1.delete(0, END)
    check.set(0)

def open_login_page():
    signup_windows.destroy()  # Close the current signup window
    
def connect_db():
    if wm1.get() == "" or un1.get() == '' or ps1.get() == '' or fps1.get() == '':
        messagebox.showerror("Error", "All Fields Are Required.")
    elif ps1.get() != fps1.get():
        messagebox.showerror("Error", "Password Does not match")
    elif check.get() != 0:
        messagebox.showerror("Error", "Please accept Terms & Conditions")
    else:
        checkm(wm1.get())
        


signup_windows = Tk()
signup_windows.title("Signup Page")
signup_windows.configure(bg="black")  # Set background color to black

sign_width = 500
sign_height = 600
signup_windows.geometry(f"{sign_width}x{sign_height}+{int((signup_windows.winfo_screenwidth() - sign_width) / 2)}+{int((signup_windows.winfo_screenheight() - sign_height) / 2)}")

# Disable window resizing
signup_windows.resizable(False, False)

frm = Frame(signup_windows, bg="black")
frm.place(relx=0.5, rely=0.5, anchor=CENTER)

heading = Label(frm, text="CREATE AN ACCOUNT", font=('Microsoft Yaei UI Light', '19', 'bold'), bg="black", fg="firebrick1")
heading.grid(row=0, column=0, pady=(10, 5))

wm = Label(frm, text="E-Mail: ", font=('Open Sans', 9), fg='white', bg='black')
wm.grid(row=1, column=0, sticky='w', padx=25, pady=(11, 0))
wm1 = Entry(frm, font=('Microsoft Yaei UI Light', 11), width=28, bd=0, fg="white", bg="firebrick1")
wm1.grid(row=2, column=0, sticky='w', padx=25)

un = Label(frm, text="User Name: ", font=('Open Sans', 9), fg='white', bg='black')
un.grid(row=3, column=0, sticky='w', padx=25, pady=(11, 0))
un1 = Entry(frm, font=('Microsoft Yaei UI Light', 11), width=28, bd=0, fg="white", bg="firebrick1")
un1.grid(row=4, column=0, sticky='w', padx=25)

ps = Label(frm, text="Password: ", font=('Open Sans', 9), fg='white', bg='black')
ps.grid(row=5, column=0, sticky='w', padx=25, pady=(11, 0))
ps1 = Entry(frm, font=('Microsoft Yaei UI Light', 11), width=28, bd=0, fg="white", bg="firebrick1", show="*")
ps1.grid(row=6, column=0, sticky='w', padx=25)

fps = Label(frm, text="Confirm Password: ", font=('Open Sans', 9), fg='white', bg='black')
fps.grid(row=7, column=0, sticky='w', padx=25, pady=(11, 0))
fps1 = Entry(frm, font=('Microsoft Yaei UI Light', 11), width=28, bd=0, fg="white", bg="firebrick1", show="*")
fps1.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()
cs = Checkbutton(frm, text='I agree to The Terms & Conditions', font=('Open Sans', 9, 'bold'), bg='white', fg='black', variable=check)
cs.grid(row=9, column=0, sticky='w', padx=22, pady=(11, 0))

logbt = Button(frm, text='Signup', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', activebackground='firebrick1', cursor='hand2', bd=0, width=17, command=connect_db)
logbt.grid(row=10, column=0, padx=25, pady=11)

sinuplb=Label(frm,text="You have an account? ",font=('Open Sans',9,'bold'),fg='firebrick1',bg='black')
sinuplb.grid(row=11,column=0,sticky='w',padx=25,pady=11)
newbt=Button(frm,text='Log in',font=('Open Sans',9,'bold underline'),fg='blue',activebackground='black',cursor='hand2',bd=0,bg='black',command=open_login_page)
newbt.place(x=165,y=360)

signup_windows.mainloop()
