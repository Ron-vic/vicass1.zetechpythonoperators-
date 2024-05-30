#PYTHON PROJECTS ASSIGNMENT-BSCIT-05-0389/2022

#1.Python program to prompt user for hours and rate per hour to compute gross pay
user=(input("Enter your name :"))
hours=int(input("Enter the Amount of hours worked :"))
rate=float(input("Enter Rate per hour :"))
Gross_pay=hours*rate
print("Users Name :" +user)
print(hours)
print(rate)
print(Gross_pay)


#2.Python program that will offer a customer a loan if they are 21 years or over and hava an annual income of 21000.

Name=(input("Enter yor name :"))
Age=int(input("Your age :"))
Income=int(input("Enter your Annual Income :"))
if Age >=21 and Income >=21000 :
    print("Congratulation You qualify for a loan")
else:
    print("Unfortunatly,we are unable to offer you a loan this time")


#3.Python program that will check if a number is divisible by 5,7,11,even

number=int(input("Enter a number :"))

if number % 5 == 0:
       print("This number is divisible by 5")
elif number % 7 == 0:
        print("This number is divisible by 7")
elif number % 11 == 0:
        print("This number is dividble by 11")
elif number % 2 == 0:
        Print("This is an even number")
else:
    print("this number is not dvisible by 5,7,11 or is not an even number")


#4.Python program that will compare the height of three students

name1=(input("Enter user name :"))
num1=int(input("Enter height :"))
name2=(input("Enter user name :"))
num2=int(input("Enter height :"))
name3=(input("Enter user name :"))
num3=int(input("Enter height :"))

print(name1  ,num1)
print(name2  ,num2)
print(name3  ,num3)

if (num1 >= num2) and (num1 >= num3):
   print(name1 ,"Is the Tallest")
elif (num2 >= num1) and (num2 >= num3):
   print(name2 ,"is the Tallest")
else:
   print(name3 ,"is  the Tallest")
