total =240
obtaied = float(input("Ënter obtained marks: "))
n = int(input("Enter the no. of subjects: "))
for i in range(n):
    marks = int(input("Enter marks of each subject: "))
    total += marks

cgpa = (obtaied/total) * n
print("Total CGPA", cgpa)

