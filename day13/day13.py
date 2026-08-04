#matplotlib

import matplotlib.pyplot as plt

# x= [1,2,3,4]
# y= [1,4,9,16]
# plt.plot(x,y)
# plt.show()

#line chart
# months= ["jan","feb","mar","apr","may"]
# sales= [200,250,400,350,450]
# plt.plot(months,sales, marker= "o",markersize=10, color= "red", linestyle= '--')
# plt.title("monthly sales")
# plt.xlabel('months')
# plt.ylabel("sales")
# plt.grid()
# plt.show()

#bargraph use to compare values
products= ['laptop','smartphones','tablets','headphones','smartwatch']
sales= [150,300,200,100,80]
plt.bar(products,sales,  color= "skyblue", edgecolor= 'green', width=0.5)
plt.title("product sales")
plt.xlabel('products')
plt.ylabel("number of sales")
plt.grid(axis='y', linestyle='--',alpha=1) #alpha- shows transparency
plt.show()

