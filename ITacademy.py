import sys
import csv
import os.path


def course_inquiry():
    f=open("python.txt","r")
    if f.mode=='r':
        contents=f.read()
        print(contents)
    goback=input("Enter q to goback to main menu or Enter anykey to exit from App")
    if goback=="q":
        startFunction()
    else:
        sys.exit()

def registration():
    name=input("Enter Your Full Name: ")
    email=input("Enter your Email:")
    phone_no=input("Enter your phone number: ")
    course=input("Enter one of Above course")
    address=input("Enter your Adress")
    paymentmethod=input("How you want to make payment? To make full payment Enter full or for half payment enter half")
    if paymentmethod== "full":
        fullpay=True
        halfpay=False
    else:
        halfpay=True
        fullpay=False
    filename = '/home/tanka/Desktop/Python-assignment-3/userinformation.csv'
    fileEmpty = os.stat(filename).st_size == 0  
    with open(filename, 'a+', newline='') as csvfile:
        fieldnames = ['Name','Email','Phone_No','Course',"Address","FullPay","HalfPay"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if fileEmpty:
            writer.writeheader()
        #writer.writerow({'Name':name,'Email':email,'Phone_No':phone_no,'Course':course,"Address":address,"FullPay":fullpay,"HalfPay":halfpay})
        user_info={
            'Name':name,
            'Email':email,
            'Phone_No':phone_no,
            'Course':course,
            "Address":address,
            "FullPay":fullpay,
            "HalfPay":halfpay
            }
        writer.writerow(user_info)
            
    print("Your are sucessfully register your account.\nYou can visualize your data and update if its neccessary after \nreturning to main menu")
    goback=input("Enter q to goback to main menu or Enter anykey to exit from App")
    if goback=="q":
        startFunction()
    else:
        sys.exit()
def update_information():
    user_name=input("Enter your name")
    with open('userinformation.csv') as fd:
        reader=csv.reader(fd)
        for row in reader:
            if row[0]==user_name:
                if row[6]=="True":
                    print("Your half payment is still there")
    
        
        
def detail_information():
    user_name=input("Enter your name")
    with open('userinformation.csv') as fd:
        reader=csv.reader(fd)
        for row in reader:
            if row[0]==user_name:
                print("Your Informarion")
                print("Name : ",row[0])
                print("Email : ",row[1])
                print("Phone No : ",row[2])
                print("Course : ",row[3])
                print("Address: ",row[4])
                if row[5]=="True":
                    print("No due left. Your payment is fully sucessfull")
                else:
                    print("Your second installments is still pending. Please make your full payment before completion of course")
            else:
                print("No information about {} in the file".format(user_name))
    goback=input("Enter q to goback to main menu or Enter anykey to exit from App")
    if goback=="q":
        startFunction()
    else:
        sys.exit()
def delete_information():
    pass



def startFunction():
    print("\t\twelcome to the IT acedamy")
    courses=['Python','C#','JAVA',"Data Science"]
    print("\t The avaiable courses in our Acadamy are:")
    for course in courses:
        print("\t\t",course)
    print("Please Choose your Options")
    print(" 1. Inquiry About The Courses \n 2. Registration \n 3. Udpate Information \n 4. Details Information \n 5. Delete")
    choice=int(input("Enter your option"))
    if choice>0 and choice<5:
        if choice==1:
            course_inquiry()
        elif choice==2:
            registration()
        elif choice==3:
            update_information()
        elif choice==4:
            detail_information()
        else:
            delete_information()
    else:
        print("Please Enter correct option")

        
if __name__=="__main__":
    startFunction()
