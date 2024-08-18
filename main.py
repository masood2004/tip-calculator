print("Welcome to the tip Calculator!")

total_bill = float(input("What was the total bill? Rs."))
tip = float(input("How much tip would you like to give? Rs."))
bill_after_tip = total_bill * (tip / 100)
number_of_people = float(input("How many people to split the bill? Rs."))

bill_divided = round(float((total_bill + bill_after_tip)/number_of_people), 2)

print(f"Each Person should pay: Rs.{bill_divided}")