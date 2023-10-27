import ipdb

def calculate_tip(total_bill, percentage_tip, number_of_people):
  total_tip = int(total_bill) * (0.01 * float(percentage_tip))
  individual_tip = round(total_tip / int(number_of_people), 2)
  return round(individual_tip, 2)

end = False

while not end:
  print("Welcome to the tip calculator!")
  total_bill = input("What was the total bill?\n")[1:]
  percentage_tip = input("What percentage of tip would you like to give? 10, 12, or 15?\n")
  number_of_people = input("How many people to split the bill?\n")
  tip = calculate_tip(total_bill, percentage_tip, number_of_people)

  print(f"Each person should pay: ${tip}")
  end = True
  # response = input("Would you like to calculate the tip for another amount? Y/n")



