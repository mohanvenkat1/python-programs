def fibno(n):
	if n<=1:
		return n
	else : 
		return (fibno(n-1) + fibno(n-2))
num=int(input("Enter a number : "))
print("Fibonoci series are : ")
for i in range(num):
	print(fibno(i))
