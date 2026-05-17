list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = list(set(list1) & set(list2))

print("List 1         :", list1)
print("List 2         :", list2)
print("Common Elements:", sorted(common))