multiples_3 = set()
multiples_5 = set()


for num in range(1, 31):
    if num % 3 == 0:
        multiples_3.add(num)
    if num % 5 == 0:
        multiples_5.add(num)

print("Multiples of 3: ", multiples_3)
print("Multiples of 5: ", multiples_5)

print("Union: ", multiples_3.union(multiples_5))
print("Intersection: ", multiples_3.intersection(multiples_5))