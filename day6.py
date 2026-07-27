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



college={
      "bitm":{
    "s001":{
      "name1":"misti",
      
      "python":90,"maths":56,"dsa":67,"os":56,
   },
   "s002":{
       "name2":"astha",
       "python":93,"maths":58,"dsa":60,"os":54,
   }
      }   
}

print(college.get("student1").get("name1"))