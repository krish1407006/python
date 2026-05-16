# instance and class variables in python


class employee:
    company_name = "Apple"

    def __init__(self, name, ):
        self.name = name
        self.raise_amount = 0.2
    def display(self):
        print(f"The name of the employee {self.name} and the raise for the employee is {self.raise_amount} and the company is {self.company_name}")



emp1 = employee("krish")
emp1.raise_amount = 0.3
emp1.compan1y_name = "Google"
emp1.display()
emp2 = employee("harry")
emp2.display()