# #loops:

# for i in range(5):
#     for j in range(5):
#         print('*',end= " ")#vertically print garna help garxa
#     print()#breaks line



# for i in range(6):
#     for j in range(i):
#       print("*",end= " ")
#     print()#print right angle triangle

'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

'''

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()



# for i in range(5):
#     for j in range(i):
#         print(" ",end=" ")#space print

#     for j in range(5-i):
#         print("*", end=" ")
#     print()#prints *

# for i in range(6):
#     for j in range(6-i):
#         print(" ",end="")

#     for j in range(i):
#         print("*", end=" ")
#     print()#prints 1,3,5,7,9 *


# n=5
# for i in range(n): #i controlls row number
#     for j in range(n-i-1): #
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*", end=" ")
#     print()


#upper half
# n=5
# for i in range(n): #i controlls row number
#     for j in range(n-i-1): #
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*", end=" ")
#     print()
# #lowerhalf
# n=5
# for i in range(n-2, -1,-1): 
#     for j in range(n-i-1): #
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*", end=" ")
#     print()
 #assignments

for i in range(5):
    for j in range(9):
        if j == 4-i or j == 4+i or i == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()