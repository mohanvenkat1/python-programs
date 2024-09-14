a=int(input("Enter first side of triangle : "))
b=int(input("Enter second side of triangle : "))
c=int(input("Enter third side of triangle : "))
if a+b>c and a+c>b and b+c>a:
	print(" valid triangle...")
else:
	print("Invalid triangle...")
