class Add:
	def __init__(self,f,s):
		self.first=f
		self.sec=s
	def Display(self):
		print("First number : ",self.first)
		print("Second number : ",self.sec)
		print("Sum = ",self.first+self.sec)
dc = Add(10,20)
dc.Display()
