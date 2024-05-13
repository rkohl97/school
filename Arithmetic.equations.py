print(3+3)
print(3+3-3)
print(3+3*3)
print(3/3-3)
print(3//3)
print(3//3-3)


weight = input("Enter your weight")
unit = input("Enter the Unit L(bs) or K(gs)")

if unit.upper() == "L":
    converted = int(weight)*.45
    print(f"you are {converted} kgs")
else:
    converted = int(weight)/.045
    print(f"you are {converted} pounds")
