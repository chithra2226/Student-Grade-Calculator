print("Welcome to Student Grade Calculator")
name = str(input("Enter Name: "))
reg = int(input("Register Number: "))
dept= str(input("Dept Name: "))
college= str(input("College Name: "))
age = int(input("Age: "))
cgpa = float(input("CGPA: "))
m1 = int(input("Math: "))
m2 = int(input("Physics: "))
m3 = int(input("Chemistry: "))
m4 = int(input("English: "))
m5 = int(input("Python: "))
total = m1 + m2 + m3 + m4 + m5
average = total / 5
def grade(averages):
    if averages >= 90:
        return "o"
    elif averages >= 80:
           return "A"
    elif averages >= 70:
        return "B"
    elif averages >=50:
        return "C"
    else:
        return "Fail"
def student_report(file=None):
    print("------STUDENT REPORT------",file=file)
    print("Name           :",name,file=file)
    print("Register Number:",reg,file=file)
    print("Department:",dept,file=file)
    print("College Name:",college,file=file)
    print("Age:",age,file=file)
    print("CGPA:",cgpa,file=file)
    print("Total          :",total,file=file)
    print(f"Average        : {average:.2f}",file=file)
    print("Grade          :" ,grade(average),file=file)
    print("------------------------------",file=file)
student_report(None)

#file handling

with open(r"C:\Users\chith\PycharmProjects\AI-Fullstack\projects\01-Student_grade_calculator/student_result.txt", "w") as file:
      (student_report(file))