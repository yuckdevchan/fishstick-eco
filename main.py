def team_trees():
    int(input("How many trees do you plant? "))


def tardis():
    time_units = {
        "days": 1,
        "weeks": 7,
        "months": 31,
        "years": 365,
        "decades": 3650
    }

    handbrake = input("How much time do you let pass? e.g: '3 years', '2 days', '10 decades' ")
    # verify time unit is in the dictionary
    if handbrake.split(" ")[1] not in time_units:
        print("That's not a valid time unit!")
        tardis()
    # verify time amount is a float or integer
    try:
        int(handbrake.split(" ")[0])
    except ValueError:
        print("That's not a valid time amount!")
        tardis()
    handbrake = handbrake.split(" ")
    time_unit = handbrake[1]
    time_amount = int(handbrake[0])
    time_passed = time_units[time_unit] * time_amount  # find time passed in days
    return time_passed


def init_():
    team_trees()
    tardis()


init_()
