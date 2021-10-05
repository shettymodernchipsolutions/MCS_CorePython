a = int(input("Enter the price: "))
list = [True if a in range(2,10) else False]
if list[0] == True:
    print("In Range")
else:
    print("Not in Range")

a = int(input("Enter the number: "))
list = [True if a in range(2,10) else False]
if list[0] == True:
    print("In the Range")
else:
    print("Not in the Range")

a = int(input("Enter the number:"))
def price_range(a):
    if a in range(2,9):
        print("In the range")
    else:
        print("Not in the range")
price_range(a)
