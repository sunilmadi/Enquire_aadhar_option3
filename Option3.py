from pymongo import MongoClient
from Modules_Packages.aadhar_project import otpcheck as otpt,smsdt as smdt,emaildt as emdt
def func():
    aadhari=int(input("ENTER YOUR AADHAR NUMBER: "))
    client=MongoClient('localhost',27017)
    db=client['AADHAR']
    conn=db.AADHARINFO
    cursor=conn.find_one({'AADHARNUM':aadhari})
    if cursor is None:
        print("NO AADHAR DETAILS EXIST.PLEASE ENROLL FOR NEW AADHAR USING OPTION 1")
        return
    else:
        rt=otpt.otpcheck()
        if rt==1:            
            detail1="your pan number is : {0}, your name is : {1}, dob is : {2},city is : {3}, state is : {4}, phone number is : {5}, aadhar number is :{6}"
            detail=detail1.format(cursor['PANNUM'],cursor['NAME'],cursor['DOB'],cursor['CITY'],cursor['STATE'],cursor['PHONENUM'],cursor['AADHARNUM'])
            smdt.sendsms(detail)
            email1=input("enter your email :")
            emdt.emailfunc(email1,detail)
            return
        else:
            print("invalid OTP or time out")
            return
        


    