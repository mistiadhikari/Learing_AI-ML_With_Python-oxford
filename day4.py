# count= 1
# while count<=5:
#     print("hello")
#     count+=1

#even numbers
# num=2
# while num<=10:
#     print(num)
#     num+=2


# num=7
# unum=0
# while num!=unum:
#     unum=int(input("enter your number: "))


# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue
#     print(i)




#functions
# def greet():
#     print("hello")
# greet()
    

# def add(a,b):
#     return a+b
# print(add(5,3))

# def name(misti):
#     return misti
# print(name("misti"))


# def calculate_discount(price, discount_percent):
#     if discount_percent < 0 or discount_percent > 100:
#         raise ValueError("invalid discount")
#     return price *(1-discount_percent/100)
# print(calculate_discount(100,50))



# def c_to_f(c):
#     return c*1.8+32
# print(c_to_f(10))
# def f_to_c(f):
#     return f-32/1.8
# print(f_to_c(109))



#assignment
def student_marksheet():
    student_name = input("Enter student name: ")

    subject1 = float(input("Enter marks in English: "))
    subject2 = float(input("Enter marks in Mathematics: "))
    subject3 = float(input("Enter marks in Science: "))
    subject4 = float(input("Enter marks in Computer: "))

    total = subject1 + subject2 + subject3 + subject4
    percentage = total / 4

    print("\nSTUDENT MARKSHEET")
    print("Student Name:", student_name)
    print("English:", subject1)
    print("Mathematics:", subject2)
    print("Science:", subject3)
    print("Computer:", subject4)
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")

student_marksheet()# Calling the function