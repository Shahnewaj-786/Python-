marks = input("Please enter you marks: ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 50:
    grade = "d"
elif marks >= 30:
    grade = "C"

else:
    grade = "F"

print("ur grade is: ", grade)