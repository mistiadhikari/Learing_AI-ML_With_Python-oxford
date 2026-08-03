import numpy as np
stores=np.array([
    [120,135,150,145,160,170,180],
    [80,90,85,95,100,110,105],
    [60,55,70,65,75,80,85],
    [200,210,205,220,230,240,250],
    [150,145,160,170,180,190,200]
])
# print (np.shape(stores))


# total_product= np.sum(stores, axis=0)
# print(total_product)


# total_product_by_day=np.sum(stores, axis=1)
# print( total_product_by_day)


# print(np.max(total_product))

# print(np.max(total_product_by_day))

# print(np.average(total_product))

# print(total_product[total_product>180])

# new_product= total_product*1.10
# print(new_product)

# # new_average= np.mean(stores, axis=1)
# # print(new_average>150)

# print(np.where(total_product<150))


bonus= np.where(stores>200, 20,0)
print(bonus)