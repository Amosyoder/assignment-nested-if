# Task 1: Code Correction

weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

# Task 2: Reccomend additional clothing based on weather
add_clothes = "shorts" if weather == "sunny" else "rain jacket" if weather == "rainy" else "hat"
print(add_clothes)

# Task 3: Reccomend additional accessories based on weather
accessory = "sunscreen" if weather == "sunny" else "rain boots" if weather == "rainy" else "scarf"
print(accessory)