s1=int(input("enter the first side length of a triangle : "))
s2=int(input("enter the second side length of a triangle: "))
s3=int(input("enter the third side length of a triangle : "))
if s1+s2>=s3 and s2+s3>=s1 and s3+s1>=s2 : 
	print("it's a vaild triangle")
else :
	print("Not a valid triangle")
