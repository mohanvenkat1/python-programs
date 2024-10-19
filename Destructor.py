class Cons:
	def __init__(self):
		self.greet = "Good Morning"
	def Display(self):
		print("MSG : ",self.greet)
	def __del__(self):
		print("Object Destructed.....!!")
dc = Cons()
dc.Display()
print(dc)
del dc
