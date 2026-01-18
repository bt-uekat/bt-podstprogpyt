class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def passed(self):
        if len(self.marks) == 0:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50
    def __str__(self):
        return f"Student {self.name}, marks: {self.marks}"
student1 = Student("Adam Kowalski", [41, 71, 50])
student2 = Student("Anna Nowak", [32, 80, 23])
print(f"Did student '{student1.name}' pass?: {student1.passed()}")
print(f"Did student '{student2.name}' pass?: {student2.passed()}")