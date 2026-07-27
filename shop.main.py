import shopping
prices=[]
for i in range(5):
    item= input(f"enter item{i+1}:")
    price= float(input(f"enter price of {item}:"))

    shopping.add_item(item)
    prices.append(price)

shopping.show_item()

print("\nTotal Bill:", shopping.total_price(prices))
