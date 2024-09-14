l1=[]
n1=int(input("Enter num of ele in list1: "))
for i  in range(n1):
	ele1=input("Enter elements :  ")
	l1.append(ele1)
l2=[]
n2=int(input("Enter num of ele in list2: "))
for i  in range(n2):
	ele2=input("Enter elements :  ")
	l1.append(ele2)
con=[]
k=len(l1) if len(l1)<len(l2) else len(l2)
for i in range(k):
	con.append(l1[i]+l2[i])
print(con)
