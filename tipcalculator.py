print("Welcome to the tip calculator!")

bill = float(input("Please input the total bill: $"))

people = int(input("Please enter the number of people willing to pay the bill."))

tip = int(input("Please enter the tip you are willing to pay."))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Tip paid by each person could be ${final_amount}. ")
