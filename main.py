# You must use python 3.6 or higher to run this program
# Licensed under the GPL v2.0 ONLY. See LICENSE for details.
import random
import time


def team_trees():
    int(input("How many trees do you plant? "))


def tardis():
    time_units = {
        "days": 1,
        "day": 1,
        "weeks": 7,
        "week": 7,
        "months": 31,
        "month": 31,
        "years": 365,
        "year": 365,
        "decades": 3650,
        "decade": 3650,
        "centuries": 36500,
        "century": 36500,
        "millennia": 365000,
        "millennium": 365000
    }

    while True:
        handbrake = input("How much time do you let pass? e.g: "
                          "'2 days/weeks/months/years/decades/centuries/millenia': ")
        # verify time unit is in the dictionary
        if handbrake.split(" ")[1] not in time_units:
            print("That's not a valid time unit!")
            continue
        # verify time amount is a float or integer
        try:
            int(handbrake.split(" ")[0])
        except ValueError:
            print("That's not a valid time amount!")
        break
    handbrake = handbrake.split(" ")
    time_unit = handbrake[1]
    time_amount = int(handbrake[0])
    time_passed = time_units[time_unit] * time_amount  # find time passed in days
    return time_passed


# find out how much the trees have grown in the time passed

def let_it_grow(time_passed):
    # find out how much the trees have grown according to the average growth rate of a tree measured by the inches of
    # the circumference per year. That rate is 1.5 inches per year.
    # The rate from tree to tree should vary with a range of about 0.5 inches per year.
    growth_rate = 1.5 + random.uniform(-0.5, 0.5)
    growth = time_passed * growth_rate
    # determine how much oxygen in kg the trees produce in their lifetimes
    oxygen = growth * 0.4  # number that matthew figured out (idk)
    oxygen = oxygen / 365
    to_sender = {
        "growth": growth,
        "oxygen": oxygen
    }
    return to_sender  # minecraft uwu


def clowning_around():
    loading_quotes = (
        "Crunching Numbers...",
        "Entering the Matrix...",
        "Cracking some nuts...",
        "Flux Capacitor, Fluxing...",
        "Checking Plutonium Reserves...",
        "Photosynthesising...",
        "Rationalising Pythagoras...",
        "Mining for Diamonds..."
    )
    used_loading_quotes = [""]
    for quotes in loading_quotes:
        time.sleep(1)
        quote = ""
        while quote in used_loading_quotes:
            quote = random.choice(loading_quotes)
        print(quote)
        used_loading_quotes.append(quote)
    for i in range(0, 3):
        time.sleep(random.randint(5, 30) / 10)
        print(f"... {random.randint(200, 999999) / 100}kg?")
        time.sleep(0.3)
        print("Nah! that ain't right.")
    time.sleep(0.8)


def init_():
    team_trees()
    time_passed = tardis()
    growth = round(let_it_grow(time_passed)["growth"], 2)  # do a bit of rounding
    oxygen = round(let_it_grow(time_passed)["oxygen"], 2)  # do a bit more rounding
    # add necessary commas to number
    growth = "{:,}".format(growth)
    oxygen = "{:,}".format(oxygen)
    time_passed = "{:,}".format(time_passed)
    clowning_around()
    print(f"The trees have grown {growth} inches collectively and produced {oxygen}kg of oxygen collectively in"
          f"{time_passed} days since you last saw them! How time flies by! (smh)")


init_()
