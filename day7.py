#sets- donot accept duplicacy

# my_set= {"banana","mango","cherry"}
# print (my_set)

# my_set= {"banana","apple","mango"}
# my_set.add("orange")
# my_set.remove("apple")
# my_set.add("mango")
# print(my_set)


# set1= {"A","B", "C"}
# set2= {"B","C","D"}

# a= set1.intersection(set2)
# b=set2.union(set1)
# print(a)
# print(b)
# c= set1.difference(set2)
# print (c)


# n:set[int]={}  #initializing empty sets
# print(n)

#file handling

# file= open("fruits.txt","r")
# content = file.read() #read everthing at one all
# print(content)
# file.close()

# file= open("fruits.txt","r")
# for line in file:

#  print(line.strip()) #read line by line
# file.close()


# file= open("student.txt","w") #write the file
# file.write("ram\n")
# file.write("hari\n")
# file.write("sita\n")
# file.close()
# print("file created")

# file= open("student.txt","a")  #adds item in a file atlast
# file.write("riyaaa\n")

# file.close()
# print("file updated")

# import csv
# with open("student.csv","r") as file:
#   reader= csv.reader(file)
#   for row in reader:
#     print(row)


import csv
with open("student.csv","r") as file:
  reader= csv.reader(file)
  next (reader) #heading escape
  for row in reader:
    name = row[0]
    maths = int(row[1])
    english = int(row[2])
    social = int(row[3])
    average = (maths+english+social)/3
    print(name, average)