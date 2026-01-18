from modules import Student

student1 = Student("Adam Kowalski", [41, 71, 50])
student2 = Student("Anna Nowak", [32, 80, 23])
print(f"Did student '{student1.name}' pass?: {student1.passed()}")
print(f"Did student '{student2.name}' pass?: {student2.passed()}")
