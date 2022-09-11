
class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.fullname = firstname + ' ' + lastname
		self.email = '{}.{}@company.com'.format(firstname, lastname).lower()
    
    
    employee = Employee("hassan", "salem")
    print(employee.fullname)
    print(employee.email)
    
