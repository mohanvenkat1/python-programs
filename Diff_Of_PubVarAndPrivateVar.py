class Student:
	branch="cse"
	def read_student_details(self,rno,n):
		self.redgno=rno
		self.name=n;
	def print_student_details(self):
		print("Student redg.no : ",self.regdno)
		print("Student name : ",self.name)
		print("Student branch : ",Student.branch)
s = Student()
s.read_student_details("324234","mohith")
s.print_student_details()
print(s.__redgno)
