from bs4 import BeautifulSoup   #from models.employee import Employee
from models.fulltime_employee import FTEmployee
from webapps.web_reader import WebReader
from vector.vector import Vector


def main():
    test11()
    test22()
    test33()


def test11():
    employees = []
    print("running the main method")
    fulltime1 = FTEmployee("Employee1", "FamilyName1", 175000, "Digital")
    fulltime1.full_time_benefits()
    fulltime2 = FTEmployee("Employee2", "FamilyName2", 175000, "Digital")
    fulltime3 = FTEmployee("Employee3", "FamilyName3", 175000, "Digital")
    fulltime4 = FTEmployee("Employee4", "FamilyName4", 175000, "Digital")
    employees.append(fulltime1)
    employees.append(fulltime2)
    employees.append(fulltime3)
    employees.append(fulltime4)
    print("average salary")
    print(FTEmployee.average_salary(employees))


def test22():
    webreader = WebReader()
    raw_html = webreader.read_web_content("https://en.wikipedia.org/wiki/Deep_learning")
    soup = BeautifulSoup(raw_html, 'html.parser')
    print("title of the page {0}".format(soup.title.string))
    print("Found href links with html element a")
    number_of_links = 0
    for link in soup.find_all('a'):
        number_of_links += 1
        print(link.get('href'))
    print("number of links in a are {0}".format(number_of_links))


def test33():
    value = Vector()
    output = value.reshape(value.generate_random(15), 3, 5)
    value.replace_maxmium(output, 0, 1)



if __name__ == "__main__":
    main()
