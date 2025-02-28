#Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
#Add a new city and its dish to the dictionary.
#Update the dish for Bengaluru.
#Remove one city from the dictionary.
#Use the keys() method to print all city names in the dictionary.
#vUse the values() method to print all dishes in the dictionary.

karnataka_food = {
    "Bengaluru" : "Bisi Bele Bath",
    "Mysur" : "Mysore Pak",
    "Mangalore" : "Neer Dosa",
    "Hubballi-Dharward" : "Dharward Peda",
    "Udupi" : "Ududpi Sambar"
}
new_dish = {"bijapur" : "jolad roti"}
karnataka_food.update(new_dish)

print(karnataka_food)

karnataka_food["Bengaluru"] = "Rava idly"

print(karnataka_food)

del karnataka_food["Udupi"]
print(karnataka_food)

print(karnataka_food.keys())
print(karnataka_food.values())
