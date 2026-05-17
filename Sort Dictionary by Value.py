students = {
    'Alice': 85,
    'Bob'  : 92,
    'Eve'  : 78,
    'David': 88
}

# Sort by value (marks) in ascending order
sorted_dict = dict(sorted(students.items(), key=lambda item: item[1]))

print(sorted_dict)