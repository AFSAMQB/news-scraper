amount=int(input("Enter amount of warasat: "))
spouse=input("Is hubby/wife alive Y/N: ")
sons=int(input("How many son(s): "))
daughters=int(input("How many daughter(s)"))
if spouse == "Y":
    print("Part of wife/hubby:",amount/8)
part= amount/((sons*2)+daughters)
if sons>0:
    print("Share of each son is:",part*2)
if daughters>0:
    print("Share of each daughter is:", part)