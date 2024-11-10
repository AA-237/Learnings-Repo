from car import Car, Student

car1 = Car("Mustang", "black", 2024, False) 
car2 = Car("Corvette", "White", 2025, False) 
car3 = Car("Charger", "Red", 2026, True) 
# print(car1.color)
# car1.describe()

student1 = Student("Spongebob", 34)           
student2 = Student("Patrick", 30) 
print(student1.name)
print(student1.age)
print(Student.class_year)

print(Student.num_student)
print(f"My Graduating class of {Student.class_year} has {Student.num_student}")
print(student1.name,  student2.name)

