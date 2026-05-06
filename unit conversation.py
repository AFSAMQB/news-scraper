print("=== UNIT CONVERTER ===")
print("1. Kilometer to Meter")
print("2. Meter to Kilometer")

choice = int(input("Enter your choice (1-2): "))

# Distance conversions
if choice == 1:
    km = float(input("Enter kilometers: "))
    meter = km * 1000
    print("Meters =", meter)

elif choice == 2:
    meter = float(input("Enter meters: "))
    km = meter / 1000
    print("Kilometers =", km)

else:
    print("Invalid choice")