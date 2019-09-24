class InputHandler:
    def read_inputs(self):
        students = int(input("Enter number of students"))
        weight_kg = []
        for each in range(students):
            weight = int(input("Enter Weight(in LBS) of Student " + str(each + 1)))
            weight_kg.append(weight * 0.453592)
        return weight_kg

