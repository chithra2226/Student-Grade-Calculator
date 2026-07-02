print("Welcome to Student Grade Calculator")
name = input("Enter Name: ")
reg = input("Register Number: ")
m1 = int(input("Math: "))
m2 = int(input("Physics: "))
m3 = int(input("Chemistry: "))
m4 = int(input("English: "))
m5 = int(input("Python: "))
total = m1 + m2 + m3 + m4 + m5
average = total / 5
def grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >=50:
        return "C"
    else:
        return "Fail"

print("\n------STUDENT REPORT------")
print("Name           :",name)
print("Register Number:",reg)
print("Total          :",total)
print("Average        :",average)
print("Grade          :" ,grade(average))
