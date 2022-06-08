# Creating a new list
my_shopping_list = ['Cookies', 'Choclates', 'Chips', 'Apple', 'Grapes']

# Printing a list
print(my_shopping_list)

# Accessing an item in a list
print(my_shopping_list[2])

# Changing an item in a list
my_shopping_list[1] = 'Chocolates'
print(my_shopping_list)

# Negative Indexing
print(my_shopping_list[-2])

# Counting item in a list
print(len(my_shopping_list))


# Looping through a list
for item in my_shopping_list:
    print(item)

# Check if item exists
stuff = 'Fanta'
if stuff in my_shopping_list:
    print('Item Found')
else:
    print('Item not found')

# Adding item in a list
my_shopping_list.append('Maggie')
print(my_shopping_list)

# Removing item from a list
my_shopping_list.remove('Chips')
print(my_shopping_list)

# Deleting an item at an index
del my_shopping_list[1]
print(my_shopping_list)


# Clearing a list
my_shopping_list.clear()
print(my_shopping_list)

# Destroying the list
del my_shopping_list
# print(my_shopping_list)


# Range of Indexes
my_list = ['Goa', 'Rishikesh', 'Switzerland', 'Cape Town', 'Dubai']


# Print first two element
print(my_list[0:2])

# Print 4 elements from start
print(my_list[:4])

# start --> start from this index
# stop --> stop at stop-1
