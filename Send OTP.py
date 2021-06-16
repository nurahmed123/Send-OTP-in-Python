# Todo : Code by Bong Programiz >>>> Channel link : https://www.youtube.com/channel/UC2TmzHkWeKpEXnYxRAHdjIQ    >>>>
import random
import smtplib
from email.message import EmailMessage

try:
    msg = EmailMessage()
    msg['Subject']='Verify OTP'
    msg['From']=input("Enter tour email address : ")
    msg['To']='06nurahmed@gmail.com'

    otp =''.join([str(random.randint(1,9)) for i in range(6)])
    real_msg = 'Hello sir! \nWelcome to our software .\nYour OTP code is : '+str(otp)

    msg.set_content(real_msg)

    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('set your own email','set your own email password') # TODO : IN QUOTATION TYPE YOUR OWN EMAIL AND PASSWORD
    server.send_message(msg)
    print("OTP Successfully Send")
except Exception as e:
    error_msg = "Something is wrong . Check Your internet connection and email address . Try again"
    print(error_msg)
server.quit()
