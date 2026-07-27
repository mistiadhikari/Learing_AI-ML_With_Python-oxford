# x= 50 #gobal variable if outside the functions
# def test():

#  print(x)

# test()

# def demo():
#     z= 100 #local variables they are defined inside the function
#     print(z)

# demo()


# def change():
#     global x #comapring with upper x and printig 20 instead of 50
#     x=20
# change()
# print (x)


#datastrucuture
#list,tuple,set,dictionary


#list:
# fruits= ["Apple","mango","litchi","banana"]
# print(fruits)
# print(fruits[1:3])


#tuples:
# n=(10,20,30)
# print(n(2))



#dictionary

# student={
#     "names":{
#         "name1":"misti",
#         "name2": "riya",
#         "name3": "sunita",
#         "name4":"siya"
#     },
#     "marks":{
#         "python":90,
#         "maths":56,
#         "dsa":67,
#         "os":56
#     }
    

# }
# print(student["names"])
# print(student["marks"])




# student={

#     "student1":{
#       "name1":"misti",
#       "python":90,"maths":56,"dsa":67,"os":56,
#    },
#    "student2":{
#        "name2":"astha",
#        "python":93,"maths":58,"dsa":60,"os":54,
#    }
# }
# print(student.get("student1").get("name1"))  #nesting in dictionary



# college={
#       "bitm":{
#     "s001":{
#       "name1":"misti",
      
#       "python":90,"maths":56,"dsa":67,"os":56,
#    },
#    "s002":{
#        "name2":"astha",
#        "python":93,"maths":58,"dsa":60,"os":54,
#    }
#       }   
# }

# print(college.get("student1").get("name1"))




#assigment

students = {
    "S001": {
        "name": "Misti",
        "age": 21,
        "faculty": "BITM",
        "finance": 85,
        "computer": 90
    },
    "S002": {
        "name": "Ram",
        "age": 22,
        "faculty": "BITM",
        "finance": 80,
        "computer": 88
    },
    "S003": {
        "name": "Sita",
        "age": 20,
        "faculty": "BITM",
        "finance": 92,
        "computer": 85
    }
}

#Displaying details of all students
print("Details of all students:")
for student_id, details in students.items():
    print(student_id, details)


# Displaying details of specific student S001
print("\nDetails of S001:")
print(students["S001"])


# Updating finance marks of S001 to 95
students["S001"]["finance"] = 95

print("\nAfter updating finance marks of S001:")
print(students["S001"])


# Calculating and display total marks of each student
print("\nTotal marks of each student:")

for student_id, details in students.items():
    total = details["finance"] + details["computer"]
    print(details["name"], "=", total)


# Finding and display the student with the highest total marks
highest_student = ""
highest_total = 0

for student_id, details in students.items():
    total = details["finance"] + details["computer"]

    if total > highest_total:
        highest_total = total
        highest_student = details["name"]

print("\nStudent with highest total marks:")
print(highest_student, "=", highest_total)