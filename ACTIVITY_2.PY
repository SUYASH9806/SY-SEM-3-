class Report:
    def __init__(self, title):
        self.title = title
        self.data = []

    def add_record(self, name, age, marks):
        record = {
            "name": name,
            "age": age,
            "marks": marks
        }
        self.data.append(record)

    def calculate_average(self):
        if len(self.data) == 0:
            return 0

        total = sum(record["marks"] for record in self.data)
        return total / len(self.data)

    def generate_report(self):
        print("\n==============================")
        print("        ", self.title)
        print("==============================")

        for record in self.data:
            print("Name  :", record["name"])
            print("Age   :", record["age"])
            print("Marks :", record["marks"])
            print("------------------------------")

        print("Average Marks:", self.calculate_average())
        print("==============================")


# Main program
report = Report("Student Performance Report")

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    report.add_record(name, age, marks)

# Generate dynamic report
report.generate_report()
