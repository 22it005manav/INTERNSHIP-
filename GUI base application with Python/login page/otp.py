from tkinter import *
from tkinter import messagebox
import otpgen

otpv = otpgen.generate_otps

def verify():
    otps = otp1.get()

    try:
        if otps == otpv:
            messagebox.showinfo("Success", "OTP Verified")
            if login_window_1.winfo_exists():  # Check if the window exists before destroying
                login_window_1.destroy()
                import update
            # Add your code to handle the next step after successful OTP verification
        else:
            messagebox.showerror("Error", "Invalid OTP. Please try again. ")
            # messagebox.showerror(otpv)
    except Exception as e:
        messagebox.showerror("Error", f"Error verifying OTP: {e}")

# Tkinter GUI
login_window_1 = Tk()
login_window_1.title("Login Page")
login_window_1.configure(bg="black")
window_width = 400
window_height = 300
screen_width = login_window_1.winfo_screenwidth()
screen_height = login_window_1.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
login_window_1.geometry(f"{window_width}x{window_height}+{x}+{y}")
login_window_1.resizable(False, False)

frame_right = Frame(login_window_1, bg="black")
frame_right.pack(side=RIGHT, padx=20, pady=10)

heading = Label(frame_right, text=" OTP Verification ", font=('Microsoft Yaei UI Light', '23', 'bold'), bg="black", fg="white")
heading.grid(row=0, column=0, columnspan=2, pady=(10, 10))

otp_label = Label(frame_right, text="Enter OTP : ", font=('Open Sans', 9), fg='white', bg='black')
otp_label.grid(row=1, column=0, sticky='w', padx=25, pady=21)
otp1 = Entry(frame_right, font=('Microsoft Yaei UI Light', 11), width=28, bd=0, fg="white", bg="firebrick1")
otp1.grid(row=1, column=0, padx=100, pady=10)

verify_button = Button(frame_right, text=' Next ', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', activebackground='firebrick1', cursor='hand2', bd=6, width=17, command=verify)
verify_button.grid(row=3, column=0, padx=30, pady=20)

login_window_1.mainloop()
