#list
thislist = ["apple", "banana", "cherry","pineapple","orange","buleburry"]
print(thislist)

#ordered,changable,allow duplicatiom
#length
print(len(thislist))

#datatype
print(type(thislist))

#Access
print(thislist[0])
print(thislist[1])

#Negative index
print(thislist[-3])
print(thislist[-1])

#Range
print(thislist[1:2])
print(thislist[:2])

#item exist
if "apple" in thislist:
    print("Yes")

#Add item
thislist.append("kiwi")
print(thislist)

#remove item
thislist.remove("apple")
print(thislist)

#pop
thislist.pop(2)
print(thislist)

