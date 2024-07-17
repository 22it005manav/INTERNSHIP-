from tkinter import *
from tkinter import messagebox
import pymysql.cursors
from PIL import Image, ImageTk

def change():
    if ps1.get() == "" or un1.get() == "":
        messagebox.showerror("Empty", "Please enter password")
    else:
        try:

            # Use the with statement to ensure proper closing of the connection
            with pymysql.connect(host="localhost", user='root', password='2525', database='userdata') as con:
                mycursor = con.cursor()


                query = 'select * from data where email=%s'
                mycursor.execute(query, (un1.get()))
                row = mycursor.fetchone()
                
                if row is not None:
                    query = 'UPDATE data SET password = %s WHERE email = %s;'
                    values = (ps1.get(), un1.get())
                    mycursor.execute(query, values)
                    con.commit()  # Commit the changes to the database
                    print(mycursor.rowcount, "record(s) affected")
                else:
                    messagebox.showerror("Error", "E-mail does not exist.")

                messagebox.showinfo('Success', 'Password changed successfully!')
                signup_windows.destroy()
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Database Connectivity Issue: {str(e)}')
        finally:
            mycursor.close()

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

heading = Label(frm, text="Enter New Password ", font=('Microsoft Yaei UI Light', '19', 'bold'), bg="black", fg="firebrick1")
heading.grid(row=0, column=0, pady=(10, 5))

un = Label(frm, text="E-mail : ", font=('Open Sans', 9), fg='white', bg='black')
un.grid(row=5, column=0, sticky='w', padx=25, pady=(11, 0))
un1 = Entry(frm, font=('Microsoft Yaei UI Light', 11), width=28, bd=0, fg="white", bg="firebrick1")
un1.grid(row=6, column=0, sticky='w', padx=25)

ps = Label(frm, text="Password: ", font=('Open Sans', 9), fg='white', bg='black')
ps.grid(row=8, column=0, sticky='w', padx=25, pady=(11, 0))
ps1 = Entry(frm, font=('Microsoft Yaei UI Light', 11), width=28, bd=0, fg="white", bg="firebrick1", show="*")
ps1.grid(row=9, column=0, sticky='w', padx=25)

logbt = Button(frm, text=' Next ', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', activebackground='firebrick1', cursor='hand2', bd=6, width=17, command=change)
logbt.grid(row=10, column=0, padx=30, pady=20)

signup_windows.mainloop()
