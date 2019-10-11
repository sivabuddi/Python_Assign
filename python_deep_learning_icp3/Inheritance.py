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


class FTEmployee(Employee):

    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def full_time_benefits(self):
        print("me you would have benefits as full time employee")



def main():
    test11()



def test11():
    employees = []
    print("running the main method")
    fulltime1 = FTEmployee("Employee1", "FamilyName1", 175000, "Digital")
    fulltime2 = FTEmployee("Employee2", "FamilyName2", 175000, "Digital")
    fulltime3 = FTEmployee("Employee3", "FamilyName3", 175000, "Digital")
    fulltime4 = FTEmployee("Employee4", "FamilyName4", 175000, "Digital")
    employees.append(fulltime1)
    employees.append(fulltime2)
    employees.append(fulltime3)
    employees.append(fulltime4)
    print("average salary")
    print(FTEmployee.average_salary(employees))


if __name__ == "__main__":
    main()
