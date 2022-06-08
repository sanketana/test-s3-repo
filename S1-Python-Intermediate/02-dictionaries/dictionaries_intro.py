# Creating a new dictionary
myCar = {
    "brand": "Bugatti",
    "color": "Red",
    "top speed": "261 MPH"
}

# Printing a dictionary
print(myCar)

# Accessing an Item in a dictionary
print(myCar["top speed"])

# Change the value in a dictionary
myCar["color"] = "Flaming Yellow"
print(myCar["color"])

# Looping through a dictionary, printing the keys
for key in myCar:
    print(key)

# Looping through a dictionary, printing the keys
for key in myCar:
    print(myCar[key])

for key, value in myCar.items():
    print(key, " = ", value)

# Check if a key exist in a dictionary
if "color1" in myCar:
    print("Key found")
else:
    print("Key not found")

# Dictionary Length
print(len(myCar))

# Adding item to dictionary
myCar['fuel type'] = 'Petrol'
print(myCar)

# Removing item from a dictionary
myCar.pop('color')
print(myCar)

# Clearing a dictionary
# myCar.clear()
# print(myCar)

# Copy a dictionary
mySecondCar = myCar.copy()
print(mySecondCar)

# Destroy a dictionary
del mySecondCar
print(mySecondCar)
