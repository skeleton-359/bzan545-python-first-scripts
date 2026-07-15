# # Strings, lists, and dictionaries
#
# This file is also meant to be run a few lines at a time.
#
# Today-ish:
# * strings store text
# * string methods do common text chores
# * lists store ordered values
# * indexes pull one value
# * slices pull several values
# * lists can be modified
# * dictionaries store key-value pairs
# * dictionaries can be modified
# * nested values mean values inside values
# * f-strings help build readable strings from variables

# A string is text. Use quotes around string values.
name = "Adam"
sentence = "The rain in Spain falls neatly on the plain."

print(name)
print(sentence)

# Many Python objects have methods. A method is a function attached to an object.
# Some useful string methods:
# * .upper()
# * .lower()
# * .split()
# * .strip()
#
# Type a few string method examples here:

print(name.upper(), name.lower(), sentence.split(" "), sentence.strip())

# What's a case where you might want .lower() or .upper()?
# When you are cleaning data and want to merge duplicates with different cases.

# What's a case where you might want .strip()?
# To get rid of characters like spaces, tabs or returns.

# What's a case where you might want .split()?
# If you want to isolate parts of a string for data manipulation.

# A list is an ordered collection of values.
products = ["hoodie", "cap", "mug", "sticker"]
print(products)

# Python starts counting at 0.
# Indexing:
# * products[0] is the first item
# * products[1] is the second item
# * products[-1] is the last item
#
# Pull a few products here:
print(products[0:3])
print(products[-2:-1])

# Slicing pulls multiple values.
# Slicing shape:
# * list[start:stop]
# * start is included
# * stop is not included
# * list[start:stop:step] can skip values
#
# Type a few indexing/slicing examples here:
products[0:4:2]
# What do you think products[1:3] will return?
# items 2 and 3.

# What do you think products[:2] will return?
# the first 2 items.

# What do you think products[::2] will return?
# every other item starting with the first.

# Lists can change.
# * .append() adds one item
# * .extend() adds several items
# * + can combine lists into a new list
# * assigning by index replaces an item

# Try adding one product:
products.append("socks")
# Try adding several products:
products.extend(("tie", "keychain"))
products
# Try combining two lists:
apparel = ["hoodie", "cap"]
home = ["mug", "blanket"]

apparel + home

# Try replacing one item in products:

products[-1] = "VOLveralls"

# Beginner object gotcha:
# Two names can point to the same list object.
products_a = ["hoodie", "cap"]
products_b = products_a

# Try appending to products_b, then print both products_a and products_b.

products_b.append("water bottle")
print(products_a, products_b)


# Try again with .copy().
products_a = ["hoodie", "cap"]
products_b = products_a.copy()

# Try appending to products_b, then print both products_a and products_b.

products_b.append("water bottle")
print(products_a, products_b)

# Getting crazy
a = [["hoodie"], ["cap"]]
b = a + [["socks"], ["mug"]]
b[0].append("orange")

print(b)
print(a)

# len() gives the length of many Python objects.
print(len(products))
print(len(name))

# f-strings let us put variable values inside strings.
# Start the string with f and put variable names inside curly braces.
origin = "knx"
destination = "atl"
ship_date = "2026-07-14"

# Type an f-string example here:
print(f"origin: {origin}")


# A dictionary stores key-value pairs.
# You look values up by key.
# Dictionary shape:
# * "name" is a key
# * "Terry" is a value
# * student["name"] looks up the value for the "name" key
student = {
    "name": "Terry",
    "age": 30,
    "is_student": False,
    "grades": [90, 92, 89],
}

# Type a few dictionary examples here:
Ingredients = {
    "Flour": 1.5,
    "Sugar": "3 tbsp",
    "has_eggs": True,
}
# Pull the student's name:
student["name"]
# Pull the student's grades:
student["grades"]
# Pull the student's first grade:
student["grades"][0]
# Pull the student's last grade:
student["grades"][-1]
# Calculate the student's average grade:
sum(student["grades"]) / 3
# Explore the dictionary:
# * .keys()
# * .values()
# * .items()
student.keys()
student.values()
student.items()
# Dictionaries can change.
# * assigning to a new key adds a key-value pair
# * assigning to an existing key replaces that value

# Try adding a major:
student["major"] = "Music"
# Try changing the student's age:
student["age"] = 22
student
# Do dictionaries have the same two-names-one-object behavior as lists?
student_a = {
    "name": "Terry",
    "grades": [90, 92, 89],
}
student_b = student_a

# Try changing student_b["name"], then print both student_a and student_b.


# Try again with .copy().
student_a = {
    "name": "Terry",
    "grades": [90, 92, 89],
}
student_b = student_a.copy()

# Try changing student_b["name"], then print both student_a and student_b.
#
# Note for later: .copy() is enough for this simple top-level change.
# Nested values like the grades list need a little more care.

# Mini task: order dictionary
order = {
    "product": "Rocky Top Mug",
    "quantity": 3,
    "unit_price": 16,
}

# Calculate order_total using the order dictionary:


# Practice prompts
#
# 1. Add a new product to the products list with products.append(...).
#
# 2. Create two product lists, combine them, then replace one item.
#
# 3. Add a new key to the student dictionary.
#
# 4. Print the type of products and student.
#
# 5. A SKU looks like "APP-HOODIE-XL-ORANGE".
#    Store it in a variable, split it on "-", and print the product part.
#
# 6. A messy customer name is "   pat summit   ".
#    Clean it so it prints as "PAT SUMMIT".
#
# 7. Given order_totals = [48, 16, 72, 24], print the first order,
#    the last order, and the first two orders.
#
# 8. Create a dictionary for an order with product, quantity, and unit_price.
#    Calculate and print the order total from the dictionary values.
#
# 9. A customer record has first name, last name, email, and state.
#    Store it as a dictionary and print a one-line shipping label.
#
# 10. A route code looks like "knx-atl-2026-07-14".
#    Split it into pieces and print:
#    "shipping from knx to atl on 2026-07-14"
#    Use split, indexing/slicing, and either an f-string or string concatenation.
