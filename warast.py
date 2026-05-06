#correct logically code
amount = int(input("enter amount of warasat"))
spouse = input("is hubby/wife alive? (Y/N)")
sons = int(input("how many son(s)"))
daughters = int(input("how many daughter(s)"))
if spouse == "Y":
    print("part of hubby/wife", amount/8)
    amount = amount - (amount/8)
part = amount/((sons*2)+daughters)
print("share of each son is", part*2)
print("share of each daughter", part)


#wednesday work inheritance
amount=int(input("enter amount of warasat"))
spouse=input("is hubby/wife alive Y/N")
sons=int(input("how many son(s)"))
daughters=int(input("how many daughter(s)"))
if spouse == "Y":
    print("part of wife/hubby:",amount/8)
part= amount/((sons*2)+daughters)
if sons>0:
    print("share of each son is:",part*2)
if daughters>0:
    print("share of each daughter is:", part)