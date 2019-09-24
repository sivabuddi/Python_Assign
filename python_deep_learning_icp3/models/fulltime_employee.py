from employee import Employee


class FTEmployee(Employee):

    def __init__(self, name, family_name, salary, department):
        super(FTEmployee, self).__init__(name, family_name, salary, department)

    def full_time_benefits(self):
        print("me you would have benefits as full time employee")
