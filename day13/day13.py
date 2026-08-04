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
# products= ['laptop','smartphones','tablets','headphones','smartwatch']
# sales= [150,300,200,100,80]
# plt.bar(products,sales,  color= "skyblue", edgecolor= 'green', width=0.5)
# # for i, value in enumerate (sales):
# #     plt.text(i, value,str(value), ha= 'center',va= 'bottom',fontsize= 10)
# # plt.barh(products,sales) for horizintal represnttion
# plt.title("product sales")
# plt.xlabel('products')
# plt.ylabel("number of sales")
# plt.grid(axis='y', linestyle='--',alpha=1) #alpha- shows transparency
# plt.show()



#piechart- to represent data in % form

# expenses= [2200,2350,2600,2130,2190]
# categories= ['rent','gas','food','clothes','misc']

# plt.pie(expenses, labels= categories, autopct='%1.1f%%')
# plt.title('monthly expenses')
# plt.show()

#scratter plot- duita number ko realtion dekhauni

# hours= [1,2,3,4,5]
# marks= [40,45,50,60,70]
# plt.scatter(hours, marks)
# plt.title("hours VS Marks")
# plt.xlabel("hours studied")
# plt.ylabel("marks obtained")
# plt.show()


#histogram: works on numerical data

# marks= [88,92,79,85,90,95,87,91,84,89,93,78,82,94,86,80,83,81,77,76]
# plt.hist(marks, bins= [0,20,40,60,80,100], edgecolor= 'black')
# plt.title("distributionof marks")
# plt.xlabel("marks")
# plt.ylabel("frequency")
# plt.show()

# months= ['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
# sales_2024= [1500,1800,2000,2200,2500,2700,3000,3200,3500,3700,4000,4200]
# sales_2025=[1600,1900,2100,2300,2600,2800,3100,3300,3600,3800,4100,4300]
# plt.plot(months,sales_2024, label= 'sales 2024',marker='o')
# plt.plot(months,sales_2025, label= 'sales 2025',marker='o')
# plt.title('monthly sales comparison')
# plt.xlabel('months')
# plt.ylabel('sales')
# plt.legend()
# plt.show() #multiline graph


months= ['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
sales_2024= [1500,1800,2000,2200,2500,2700,3000,3200,3500,3700,4000,4200]
sales_2025=[1600,1900,2100,2300,2600,2800,3100,3300,3600,3800,4100,4300]
product=['laptop','smartphone','tablet','headphones','smartwatch']
#basic line chart
# plt.plot(months,sales_2024, marker= "o",markersize=10, color= "red", linestyle= '--')
# plt.title("sales in 2024")
# plt.xlabel('months')
# plt.ylabel("sales")
# plt.grid()
# plt.show()

#multiline chart
# plt.plot(months,sales_2024,sales_2025, marker= "o",markersize=10, color= "purple", linestyle= '--')
# plt.title("sales in 2024 & 2025")
# plt.xlabel('months')
# plt.ylabel("sales")
# plt.grid()
# plt.show()


#vertical barchart
# plt.bar(months,sales_2024,  color= "purple", linestyle= '--')
# plt.title("sales in 2024")
# plt.xlabel('months')
# plt.ylabel("sales")
# plt.grid()
# plt.show()


#horizontal barchart
# plt.barh(months,sales_2025,  color= "purple", linestyle= '--')
# plt.title("sales in 2024")
# plt.xlabel('months')
# plt.ylabel("sales")
# plt.grid()
# plt.show()



#histogram 

plt.hist(sales_2025, edgecolor= 'black')
plt.title("sales in 2025")
plt.xlabel("sales")
plt.ylabel("frequency")
plt.show()