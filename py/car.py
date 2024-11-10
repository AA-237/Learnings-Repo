 
class Car():
    def __init__(self, model, color, year, for_sale):
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You are driving the {self.model}")
    def stop(self):
        print(f"You stopped the {self.model}")        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")    
        
class Student: 
    
    class_year = 2014
    num_student = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1
          