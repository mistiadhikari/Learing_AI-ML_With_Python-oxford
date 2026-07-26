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

def employee(**details):
    for key,value in details.items():
        print(key,"=",value)

employee(Name="misti", department="it",salary= 400000, country="USA")
    