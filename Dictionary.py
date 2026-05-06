#Dictionary
thisdict = {"Apple": 1, "Orange": 2, "Banana": 3, "cherry": 4, "blueberry": 5}
print(thisdict)

#length
print(len(thisdict))

#datatype
print(type(thisdict))

#Access
x = thisdict["Apple"]
print(x)

#get
#x = thisdict.get("model")

#key get

x = thisdict.keys()
print(x)

#add item key i dictionary
thisdict["pea"] = "9"
print(thisdict)

#get values
x = thisdict.values()
print(x)
#add value
thisdict["potato"] = "10"
print(thisdict)

#get item
x = thisdict.items()
print(x)

#change item
thisdict["banana"] = "11"
print(thisdict)
#update item
thisdict.update({"banana": "12"})
print(thisdict)

#pop: removes the item with the specified key name
thisdict.pop("banana")
print(thisdict)
#popitem: remove last list item
thisdict.popitem()
print(thisdict)

#loop
for x in thisdict:
    print(x)
    print(thisdict[x])

