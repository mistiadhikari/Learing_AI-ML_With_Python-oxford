# #numpy

import numpy as np
# arr=np.array([10,20,30,40,50,60]) #1D array
# print(arr.ndim)
# print(arr.size)
# print(arr.shape)
# print(arr.dtype)


# arr2= np.array([
#     [10,20,30],
#     [40,50,60]   #2D array
# ])
# print(arr2.ndim)
# print(arr2.size)
# print(arr2.shape)
# print(arr2.dtype)

# arr3= np.array([  #3D array
#     [
#         [1,2,3,4],
#         [5,6,7,8]
#     ],
#     [
#         [9,10,11,12],
#         [13,14,15,16]
#     ],
#     [
#         [17,18,19,20],
#         [21,22,23,24]
#     ]
# ])
# print(arr3.ndim)
# print(arr3.size)
# print(arr3.shape)
# print(arr3.dtype)



# arr3= np.array([  #3D array
#     [
#         [1,2,3,4],
#         [5,6,7,8]
#     ], #axis/layer-1
#     [
#         [9,10,11,12],
#         [13,14,15,16]
#     ], #layer2
#     [
#         [17,18,19,20],
#         [21,22,23,24]
#     ] #layer-3
# ])
# print(arr3.shape)



# marks= np.array([
#     [80,85,90],
#     [75,88,92],
#     [60,70,95]
# ])

# #indexing or accessing arrays

# print(marks[0]) #gives first row
# print(marks[:,1])



# arr3= np.array([  #3D array
#     [
#         [1,2,3,4],
#         [5,6,7,8]
#     ], #axis/layer-1
#     [
#         [9,10,11,12],
#         [13,14,15,16]
#     ], #layer2
#     [
#         [17,18,19,20],
#         [21,22,23,24]
#     ] #layer-3
# ])

# print(arr3[:,1,1])


#silicing in 2d array

# marks= np.array([
#    [80,85,90],
#   [75,88,92],
#   [60,70,95]
# ])
# # print(marks[:2]) #before row 2
# # print(marks[1:])  #row 1 paxi
# # print(marks[:,:2]) sabai lai herni but before 2
# print(marks[:,1:]) # 1 paxadi herni




#silicing 3D array


arr= np.array([
    [ 
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])
# print(arr[0,:, :]) #prints row 0
# print(arr[:,0,:]) #gives the data of pahilo row ko column
# print(arr[1,0,2])

#arithmetic operations
# print(arr+10)

print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.min(arr))
print(np.sum(arr))