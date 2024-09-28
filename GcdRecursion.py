def Gcdre(n1,n2):
	if n2==0:
		return n1
	else:
		return Gcdre(n2,n1%n2)
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("the GCD of",a," and ",b," is  : ",Gcdre(a,b))

