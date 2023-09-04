# You must use python 3.6 or later to run this program.
import time, random

class OxygenGaming():

  def __init__(self):
    super().__init__()

    self.time_units = {
      "1": "day",
      "2": "week",
      "3": "month",
      "4": "year"
    }

    magic = self.wizardry()
    time_unit = str(magic[0])
    tree_circ_total = float(magic[1])
    amount_of_time = float(magic[2])
    oxygen_output_kg = self.get_oxygen_frfr(time_unit, tree_circ_total, amount_of_time)
    loading_quotes = (
      "Crunching Numbers...",
      "Entering the Matrix...",
      "Cracking some nuts...",
      "Flux Capacitor, Fluxxing...",
      "Checking Plutonium Reserves...",
      "Photosynthesising...",
      "Rationalising Pythagoras..."
    )
    used_loading_quotes = [""]
    for quotes in loading_quotes:
      time.sleep(1)
      quote = ""
      while quote in used_loading_quotes:
        quote = random.choice(loading_quotes)
      print(quote)
      used_loading_quotes.append(quote)
    time.sleep(1)
    print(f"\nYour total oxygen output for your tree is approximately: ~{oxygen_output_kg}kg.")  # 🧢 hehe

  def wizardry(self):
    time_unit = input("Do you measure your tree's circumference:\n1. Every Day\n2. Every Week\n3. Every Month\n4. Every Year\n\nInput: ")

    if time_unit not in self.time_units:
      while time_unit not in self.time_units:
        time_unit = input("Invalid Choice!\n\nTry Again: ")

    amount_of_time = input(f"How many {self.time_units[time_unit]}s have you been measuring your tree's circumference? ")

    if not amount_of_time.isnumeric():
      while not amount_of_time.isnumeric():
        amount_of_time = input("Invalid Choice!\n\nTry Again: ")

    tree_circ_total = 0

    for i in range(1, int(amount_of_time) + 1):
      tree_circ = input(f"What was your tree's circumference in inches during {self.time_units[time_unit].capitalize()} {i}? ")

      while True:
          if tree_circ.isdigit():
              break
          try:
              float(tree_circ)
              break
          except ValueError:
              tree_circ = input("Invalid Choice!\n\nTry Again: ")

      tree_circ_total = tree_circ_total + float(tree_circ)

    to_sender = (
      time_unit,
      tree_circ_total,
      amount_of_time
    )

    return to_sender  # Minecraft uwu

  def get_oxygen_frfr(self, time_unit, tree_circ_total, amount_of_time):
    how_many_in_year = {
      "day": 365,
      "week": 52,
      "month": 12,
      "year": 1
    }
    if self.time_units[time_unit] in how_many_in_year:
      oxygen_output_kg = tree_circ_total * 0.4 / how_many_in_year[self.time_units[time_unit]] * amount_of_time
    else:
      for i in range(0, 100):
        print("YOU'RE A BROKIE!!!")
      oxygen_output_kg = "BROKIE IS NOT A NUMBER!"  # Woah, you brokie my program - That's Crazy.
    return oxygen_output_kg

if __name__ == '__main__':
  OxygenGaming()  # literal magic
