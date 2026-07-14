# # Variables, math, and types
#
# This file is meant to be run a few lines at a time.
# In Positron, try putting your cursor on a line and using Cmd/Ctrl+Enter.
#
# Today-ish:
# * print something
# * write comments
# * save values with variables
# * use Python like a calculator
# * check common data types
# * notice operators can behave differently with different types

# print() shows a value so humans can see it.
print("Hello from Python")

# A comment starts with #. Python ignores comments, but humans can read them.

# A variable is a name we give to a value so we can reuse it later.
# The = sign means assignment: put the value on the right into the name on the left.
revenue = 1000
cost = 800

print(revenue)
print(cost)

# Python can work like a calculator.
# * addition with +
# * subtraction with -
# * multiplication with *
# * division with /
# * integer division with //
# * remainder/modulo with %
# * exponent with **
# * square root with ** 0.5
#
# Type a few calculator examples here:

print(19 * 32)
print(43 - 23)
print(9 + 10)
print(20 / 5)
print(23 // 5)
print(23 % 5)
print(3 ** 3)
print(9 ** 0.5)

# What's a case where you might want to use //?
# If you dont want the decimal to show up/round down to nearest integer.

# What's a case where you might want to use %?
# If you want only the remainder of something to filter/sort data.

# Types are the kind of value something is.
# Common first data types:
# * int: whole number
# * float: number with a decimal
# * str: text/string
# * bool: True or False
n_orders = 25
price = 19.99
product = "Rocky Top Mug"
is_available = True

print(type(n_orders))
print(type(price))
print(type(product))
print(type(is_available))

# What data types might you already know of from other programming languages?
# From R: Factors, characters, tuples, lists, matricies

# Operators can behave differently with different types.
# * number + number does math
# * string + string glues strings together
# * string * int repeats the string
#
# Type a few operator examples here:
print(27 + 40)
print("Large " + "Pizza")
print("Nice " * 10)


# Pizza calculator (very important work in progress)
n_people = 3
slices_per_person = 5
n_pizzas = 6
slices_per_pizza = 8

Total_pizza_slices = slices_per_pizza * n_pizzas
Total_slices_eaten = n_people * slices_per_person
remaining_slices = Total_pizza_slices - Total_slices_eaten

print(remaining_slices)

# Practice word problems (too many for us to do all together....)
#
# 1. A tailgate has 10 people. Each person brings a 6 pack of soda.
#    At the end, 8 sodas are left. How many did each person drink on average?

people_at_tailgate = 10
sodas_per_person = 6
remainder_sodas = 8

total_sodas = (people_at_tailgate * sodas_per_person)
sodas_drunk = total_sodas - remainder_sodas
avg_sodasper_person = sodas_drunk / people_at_tailgate
print(avg_sodasper_person)

# 2. A warehouse has 2,000 items. If 49 percent are sold and the rest are
#    packed into boxes of 12, how many full boxes are there and how many
#    items are left unpacked?

warehouse_total = 2000
pct_sold = .49
amt_per_box = 12
total_not_sold = warehouse_total - (warehouse_total * pct_sold)
full_boxes = total_not_sold // amt_per_box
amt_unpacked = total_not_sold % amt_per_box
print(amt_unpacked)

# 3. A student buys 3 hoodies at $48 each and 2 mugs at $16 each.
#    Sales tax is 9.25 percent. What is the final total?

total_hoodies = 3
cost_per_hoodie = 48
mug_total = 2
mug_cost = 16
sales_tax = .0925
total_cost = ((total_hoodies * cost_per_hoodie) + (mug_total * mug_cost)) * sales_tax
print(total_cost)

# 4. A batch job processed 18,725 rows in 35 minutes.
#    How many rows did it process per minute on average?

batch_job = 18725
mins_total = 35
avg_per_min = batch_job / mins_total
print(avg_per_min)

# 5. A truck can carry 42 boxes. You need to ship 389 boxes.
#    How many full trucks are needed, and how many boxes are on the last truck?

truck_capacity = 42
total_boxes = 389
full_trucks = total_boxes // truck_capacity
remain_boxes = total_boxes % truck_capacity
print(full_trucks, remain_boxes)
