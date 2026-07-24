# a= int(input("enter your choice:"))
# if a>=90:
#  print("disctinction")
# elif a>=70:
#  print("first division")
# elif a>=60:
#  print("second division")
# elif a>=50:
#  print("third division")
# else:
#  print("give re-exam")

# name= str(input("enter your name"))
# social= int(input("enter your marks in social"))
# maths= int(input("enter your marks in maths"))
# english= int(input("enter your marks in english"))
# nepali= int(input("enter your marks in nepali"))
# total= maths+social+english+nepali

# percentage= (total/4)


# if social>=32 and maths>=32 and english>=32 and nepali>=32:
#     print("congratulation",name)
#     print(" you are passed")
#     print(total)
#     print(percentage)
# else:
#     print("sorry",name)
#     print("you are failed")
    

# username= input("enter your username")
# password= input("enter your password")
# if username == "admin" and password == "admin123":
#  print("access granted")
# else:
#  print("try again")

# years= int(input("enter your years of services"))
# rating= str(input("enter your rating"))
# if years>=5 and rating== "excellent":
#     print("you'll get 20percent of bonus")
# elif years<=3 and (rating== "good" or rating== "satisfactory"):
#     print("you'll get 10percent of bonus")
# else:
#     print("there is no bonus")

    #atm logic withdraw rem balance print garni
balance = 100000

withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= 0:
    print("Invalid withdrawal amount")

elif withdraw > balance:
    print("Insufficient balance")

else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Withdrawn amount:", withdraw)
    print("Remaining balance:", balance)
