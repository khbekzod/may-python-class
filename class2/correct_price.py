# spend $100 and more and get 10% discount
# spend $200 and more and get 20% discount
# if we buy for $80 - we pay $80
# if we buy for $150 - we pay $135
# we pay 10% tax

discount=0
sales_tax=0.1

def tax_func(price):
    taxes = price * sales_tax
    return taxes
def dicsount_func(price, discount):
    discount_sum = price * (discount / 100)
    return discount_sum

price=float(input("Enter price: "))
tax=tax_func(price)

if price > 100 and price <= 200:   # if price 101-200, then discount_sum=price*0.1
    discount = dicsount_func(price,10)
elif price > 200:                  # if price more than 200 then discount_sum=price*0.2
    discount = dicsount_func(price,20)

total_price = price + tax - discount

print(total_price)