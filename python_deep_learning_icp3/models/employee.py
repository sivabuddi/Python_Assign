class Employee:
    __name = ""
    __family_name = ""
    salary = 0
    __department = ""
    counter = 0

    def __init__(self, name, family_name, salary, department):
        self.__name = name
        self.__family_name = family_name
        self.salary = salary
        self.__department = department
        Employee.counter += 1

    @staticmethod
    def average_salary(employees):
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.counter
