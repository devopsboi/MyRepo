weight = float(input("Enter Weight: "))
shipping_mothod = input("Choose Shipping Method:Normal -1 Premium - 2")



#Ground Shipping

if shipping_mothod == 1:

elif weight > 10:
    cost = weight * 4.75 + 20 
    print(cost) 
elif weight > 6 and weight <= 10:
    cost = weight * 4 + 20
    print(cost)
elif weight > 2 and weight <= 6:
    cost = weight * 3 + 20
    print(cost)   
elif weight <= 2:
    cost = weight * 1.5 + 20
    print(cost)
else:
    print("Error")    


#Ground Shipping Premium
if shipping_mothod == 2:

elif weight > 10:
    cost = weight * 14.25 + 125 
    print(cost) 
elif weight > 6 and weight <= 10:
    cost = weight * 12 + 125
    print(cost)
elif weight > 2 and weight <= 6:
    cost = weight * 9 + 125
    print(cost)   
elif weight <= 2:
    cost = weight * 4.5 + 125
    print(cost)
else:
    print("Error")