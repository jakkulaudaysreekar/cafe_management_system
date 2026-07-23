menu={
     'pizza':140,
     'Burger':100,
     'coke':70,
     'Biryani':250,
     'ice_cream':50,
     'Kabab':200,
}

print("welcom to resto")
#\n for the new line
print(" pizza:140\n Burger:100\n coke:70\n Biryani:250\n ice_cream:50\n  Kabab:200")
order_total = 0
item_1=input("enter the item you want to order =")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item{item_1} has been added to your order!")
else:
    print(f"ordered item{item_1} is not avilable")

another_order = input("do u want another item? (Yes/No) ")
if  another_order =="Yes":
    item_2 =input("enter another item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to your order")
    else:
        print(f"order item {item_2}is not available")
print(f"The total amount to be payed is {order_total}")
print("Thank you visit again")





