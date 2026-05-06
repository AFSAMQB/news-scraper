print("=== MARKS AVERAGE & GRADE CALCULATOR ===")

# input marks
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

# calculate total and average
total = m1 + m2 + m3
average = total / 3

print("Total Marks =", total)
print("Average =", average)

# grade calculation
if average >= 90:
    print("Grade = A+")
elif average >= 80:
    print("Grade = A")
elif average >= 70:
    print("Grade = B")
elif average >= 60:
    print("Grade = C")
else:
    print("Grade = Fail")
