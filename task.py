

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?"))
number_of_people = float(input("How many people to split the bill?"))
result = round(((bill + (bill * (tip / 100))) / number_of_people), 2)
print(f"Each person should pay ${result}")
