import random

# Function to generate a 6-digit OTP
def generate_otp():
    ss=str(random.randint(100000, 999999))
    return ss

generate_otps=generate_otp()