class Student:
	branch="cse"
	def read_student_details(self,rno,n):
		self.redgno = rno
		self.name = n
	def print_student_details(self):
		print("Student redg no : ",self.redgno)
		print("Student name is : ",self.name)
		print("Student branch is ",Student.branch)
s=Student()
s.read_student_details("2345235","ruku")
s.print_student_details()
