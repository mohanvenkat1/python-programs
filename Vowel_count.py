s=input("Enter a string  : ")
vow={'a','e','u','i','o','A','I','E','O','U'}
count=0
str=""
for i in s:
	str=i+str
	if(str in vow):
		count=count+1
	str=""
print(count)
