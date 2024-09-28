def rfactorial(n):
	if n<=0:
		return 1
	else:
		return n*rfactorial(n-1)
num=int(input("Enter a number : "))
print("Factorial is : ",rfactorial(num))
