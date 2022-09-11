class Calculator:
    def __init__(self, n1, n2):
     self.n1 = n1
     self.n2 = n2
		
    def add(self):
     return print(self.n1 + self.n2)
	
    def subtract(self):
     return print(self.n1 - self.n2)
		
    def multiply(self):
     return print(self.n1 * self.n2)
	
    def divide(self):
     return print(self.n1 / self.n2)


calc = Calculator(20, 10)
calc.add()
calc.subtract()
calc.multiply()
calc.divide()
