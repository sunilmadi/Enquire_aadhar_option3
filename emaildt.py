from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
def emailfunc(email,detail):
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        username="sunil.kumarmadikesari@gmail.com"
        password="littlerock"
        server.login(username,password)
        msg=MIMEMultipart()
        msg['From']=username
        msg['To']=email
        msg['Subject']="WELCOME TO AADHAR SYSTEM- AADHAR DATABASE"
        body1="Your aadhar detail is: {0}"
        body=body1.format(detail)
        msg.attach(MIMEText(body))
        f=open("E:/Project/Modules_Packages/aadhar_project/aadhar.txt","w")
        f.write(body)
        f.close()
        with open("E:/Project/Modules_Packages/aadhar_project/aadhar.txt","r") as f:
            part=MIMEApplication(f.read())
            part.add_header('Content-Disposition', 'attachment', filename='aadhar.txt' )
            msg.attach(part)
            f.close()
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    except:
        print("Email connection interupted.But you token number processing is complete without email notification.")
    finally:
        print("Your token number processing is complete.")
    
