#positional arguments
# def add(a,b,c):
#     return a+b+c
# print(add(10,20,30))

# def add(*numbers):
#     return sum(numbers)
# print(add(10,20,30))

# def fruits(*items):
#     print(items)
# fruits("apple","banana","mango","litchi")

#looping in function

# def display(*args):
#     for value in args:
#         print(value)
# display(12,34,5,7)

# def add(*numbers): #function to add unlimited numbers..
#     total= 0
#     for num in numbers:
#        total+= num
#     return total
# print(add(10,20,90))


#real world problem

# def shopping_cart(*items):
#     print("purchased items")
#     for item in items:
#         print(item)
        
# shopping_cart("bags","shoes","cap","dress")



# def student(**kwargs):
#     print(kwargs)

# student(name="misti",age=21,city="bhairawaha")

# def student(**kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])
    


# student(name="misti",age= 21)



# def student(**kwargs):
#     for key, value in kwargs.items():
#         print(key,"=",value)

# student(name= "misti", age= 14, city= "bhw")


#real world use of **kwargs

# def employee(**details):
#     for key,value in details.items():
#         print(key,"=",value)

# employee(Name="misti", department="it",salary= 400000, country="USA")



#lambda function
# def square(x):
#     return x*x
# print(square(6))


# square= lambda x:x*x#lambda
# print(square(5))


# multiply= lambda x,y : x*y
# print(multiply(4,3))


# def calculate_salary(hours,rate):
#     salary= hours*rate
#     tax= salary*0.1
#     final_salary = salary-tax
#     return final_salary
# print(calculate_salary(9,200)) #cannot be used in lambda




#sorting data using lambda

# student= [
#     ("ram",78),
#     ("hari",92),
#     ("sita", 85)
#  ]
# student.sort(key= lambda student:student[1]) #sorting using marks
# print(student)


#lambda with map()

# marks= [50,60,70,80]
# new_marks=[]
# for mark in marks:
#     new_marks.append(mark+5)
# print(new_marks)


# new_markks=list(map(lambda x:x+5,marks))
# print(new_markks)


#filtering'''
# marks= [50,60,70,80,67,32,54,90,100]
# passed=list(filter(lambda x:x>60, marks))

# print(passed)


from functools import reduce
numbers= [10,20,30,40]
total = reduce(lambda x,y:x+y,numbers) #reduce takes 2 numbers and give their sum
print( total)