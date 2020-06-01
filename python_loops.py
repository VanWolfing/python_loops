"""
Checks weather the tea is cool enough.
In order to drink the tea it needs to be over 90 degrees but not less than 50 degrees.
"""


def check_tea_temp(temp):
    # Can't drink tea if the temperature is still boiling but it can't be too cold.
    if (temp < 50):
        return "Tea is too cold!"
    while temp > 90:
        print("Tea needs to cool down!")
        temp -= 1
    return "Tea is ready to be drunk!"


"""
Checks which teas are ready to be drunk from the selected list of teas.
The method will not cool down the already existing teas only checking their temperature.
"""


def sort_drinkable_teas(teas, temp):
    # Sort out the list of teas where the temperature is less than or equal to the required temperature.
    valid_teas = []
    for tea in teas:
        if tea <= temp:
            valid_teas.append(tea)
    if len(valid_teas) == 0:
        return "No teas were cold enough"
    return valid_teas


if __name__ == '__main__':
    # Check tea temp
    print(check_tea_temp(20))  # Tea is too cold!
    print(check_tea_temp(50))  # Tea is ready to be drunk
    print(check_tea_temp(100))  # Tea needs to cool down (This happens 10 times), Tea is ready to be drunk

    # Sort teas
    teas = [100, 20, 50, 80, 40, 99, 25, 45]
    print(sort_drinkable_teas(teas, 50))  # 20, 50, 40, 25, 45
    print(sort_drinkable_teas(teas, 30))  # 20, 25
    print(sort_drinkable_teas(teas, 10))  # No teas were cold enough
