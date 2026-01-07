talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lot = float(input("Enter lot: "))



#* 1 talents = 20 * 32 * 13,3 grams
#* 1 pounds = 32 * 13,3 grams

grams = lot * 13.3 + (pounds * 32 * 13.3) + (talents * 20 * 32 * 13.3)

kgs = grams / 1000

rounded_kgs = int(kgs)

remaining_grams = grams - rounded_kgs * 1000

print("The weight in modern units:")
print(f"{rounded_kgs} kilograms and {round(remaining_grams)} grams")
