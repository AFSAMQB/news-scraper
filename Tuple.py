#Tuple
thistuple = ("apple","banana", "orange","kiwi","pineapple","cherry")
print(thistuple)

#lenght of tuple
print(len(thistuple))

#datatype
print(type(thistuple))

#positive index
print(thistuple[1])

#negative index
print(thistuple[-1])

#range
print(thistuple[2:5])
print(thistuple[2:])
print(thistuple[:-2])

#check if item exists
if "kiwi" in thistuple:
    print("Yes")

#change item
thistuple = ("apple", "banana", "orange", "cherry")
x = thistuple
y = list(x)
y[1] = "kiwi"
#Add item
y.append("pineapple")
#remove item
y.remove("cherry")
x = tuple(y)
print(x)

#unpake tuple
thistuple = ("apple", "banana", "orange", "cherry")
(red,yellow,orange,red) =thistuple
print(red)
print(yellow)
print(orange)
print(red)

#Asterisk
#red,yellow,*blue

#loop
for x in thistuple:
    print(x)

#join tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



