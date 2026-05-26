class Student:
    school = "SMIT Peshawar Student Report"
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def report(self):
        return (f"-------- {self.school} Report ----\n"
                f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Average: {self.average():.2f}\n"
                f"Grade: {self.grade()}")
    
    def __str__(self):
        return f"Student:{self.name}, Roll No: {self.roll_no}"
    
std1 = Student("Ali", 102, [85, 90, 78, 95])
std2 = Student("Sara", 105, [92, 88, 91, 89])
print(std1.report())
print(std2.report())