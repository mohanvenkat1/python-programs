string=input("Enter a string : ")
rev_str=""
for i in string:
	rev_str=i+rev_str
print("reverse string :" ,rev_str)
if(rev_str==string):
	print("Palindrone")
else:
	print("not a palindine")
