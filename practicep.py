# Dictionary
student = {
    "name": "Keshab",
    "grade": "A",
    "year": 2025
}

print(student["name"])
student["city"] = "New York"
print(student)



names = ["Keshab", "John", "Sarah"]

names.append("Mike")
print(names)

for name in names:
    print(name)



database = ("localhost", 5432)

print(database[0])



skills = {"Python", "SQL", "Python"}

skills.add("Spark")
print(skills)



def greet(name):
    return f"Hello, {name}"

print(greet("Keshab"))



class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)


emp = Employee("Keshab")
emp.show()



try:
    print(10 / 2)
except ZeroDivisionError:
    print("Cannot divide by zero")