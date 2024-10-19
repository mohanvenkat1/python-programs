class Parent():
	def func1(self):
		print("This is first function...")
class Child1(Parent):
	def func2(self):
		print('This is second function...')
class Child2(Child1):
	def func3(self):
		print("This is third function...")
ob=Child2()
ob.func1()
ob.func2()
ob.func3()
