import random

choice = int(input("input number of digits (3 / 4): "))

digits3 = range(0,9)
digits4 = range(1,6)

match choice:
    case 3:
        comb = "".join(str(x) for x in random.choices(digits3, k=3)) #evil list comprehension
        print(comb)

    case 4:
        comb = "".join(str(x) for x in random.choices(digits4, k=4)) #evil list comprehension
        print(comb)
        