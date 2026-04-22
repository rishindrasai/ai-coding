'''
 refactor procedural code into a class-based design.
Focus Areas:
o Object-Oriented principles
o Encapsulation
Legacy Code:
salary = 50000
tax = salary * 0.2
net = salary - tax
print(net)
'''
class SalaryCalculator:
    def __init__(self, salary):
        self.salary = salary

    def calculate_tax(self):
        return self.salary * 0.2

    def calculate_net_salary(self):
        tax = self.calculate_tax()
        net_salary = self.salary - tax
        return net_salary
salary_calculator = SalaryCalculator(50000)
net_salary = salary_calculator.calculate_net_salary()
print(net_salary)
