# You must use python 3.6 or later to run this program.
time_units = {"1": "day", "2": "week", "3": "month", "4": "year"}
time_unit = input("Do you measure your tree's circumference:\n1. Every Day\n2. Every Week\n3. Every Month\n4. Every Year\n\nInput: ")

if time_unit not in time_units:
  while time_unit not in time_units:
    time_unit = input("Invalid Choice!\n\nTry Again: ")

amount_of_time = input(f"How many {time_units[time_unit]}s have you been measuring your tree's circumference? ")

if not amount_of_time.isnumeric():
  while not amount_of_time.isnumeric():
    amount_of_time = input("Invalid Choice!\n\nTry Again: ")

tree_circ_total = 0

for i in range(1, int(amount_of_time) + 1):
  tree_circ = input(f"What was your tree's circumference in {time_units[time_unit].capitalize()} {i}? ")

  if not tree_circ.isnumeric():
    while not tree_circ.isnumeric():
      tree_circ = input("Invalid Choice!\n\nTry Again: ")

  tree_circ_total = tree_circ_total + float(tree_circ)

if time_units[time_unit] is "year":
  oxygen_output_kg = float(tree_circ_total) * 0.4
else:
  for i in range(0, 100):
    print("YOU'RE A BROKIE!!!")
  oxygen_output_kg = "BROKIE IS NOT A NUMBER!"
print(f"Your total oxygen output for your tree is approximately: ~{oxygen_output_kg}kg.")

