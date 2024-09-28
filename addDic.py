def adddec(d,k,v):
	d[k]=v
	return d
	

dic={"Name":"mohanVenkat","redg":561,"sec":"A","Phone":9030669229}
print("dictonary keys and values are : ",dic)
key=input("Enter the key value:")
val=input("Enter the value: ")

print("After changing the Dic_______")
print(adddec(dic,key,val))
