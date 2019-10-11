class Parttime:
    salary=0
    counter=0
    name=""
    department=""
    # default constructor

    def __init__(self,name,salary,department):
        self.name=name
        self.department=department
        self.salary=salary
        Parttime.counter+=1

    @staticmethod
    def average_salary(emp):
        sum=0.0
        for Emp in emp:
            sum=sum+Emp.salary
        return sum/Parttime.counter


class Fulltime(Parttime):

    def __init__(self,name,salary,department):
        super().__init__(name,salary,department)


employees=[]
Ft1=Fulltime("sivakumar",10000,'cse')
Ft2=Fulltime("Rajkumar",12000,'cse')
Ft3=Fulltime("Chandra",14000,'cse')
Ft4=Fulltime("Ajit",15000,'cse')

employees.append(Ft1)
employees.append(Ft2)
employees.append(Ft3)
employees.append(Ft4)

print("Average sarlay of the employee=",Fulltime.average_salary(employees))
