#     1. What is a for loop?

# A for loop takes a collection (like a list, a file with 1,000 rows, or a range of numbers)
# and automatically grabs each item one by one. 
# It handles the "counting" and the "stopping" for you automatically.

#  In English, you say: "I have a gift for every person in this room."
    
#    In Python, the for loop says:
#    "For every item in this list, do this action."
    
#    2. The Difference (The ELI5 Analogy)
    
#    Feature: Analogy
# while loop: Like waiting for a customer to walk into your shop. 
# You stay open while they are coming.

# for loop: Like having a stack of 10 letters to sign. 
# You sign them one by one for each letter in the stack.

# Basic for loop shape 
prices = [100, 250, 300, 150]

for price in prices:
    taxed_price = price * 1.10
    print("The price with 10% tax is:", taxed_price, )

# basic range shape
for number in range(1, 6):
    print(number) 
    
parts = ['Screen', 'Keyboard', 'Battery']
for part in parts:
    print('Checking part', part)
    
 # Write a for loop that prints: "Kitchen, please start order number: [ID]" for every ID in that list.
 # but skip ID 103.
    
orders = [101, 102, 103, 104]
for order in orders:
    if order == 103:
        continue
    print('Kitchen, please order ID:', order, 'preparing')
    
order_totals = [15, 80, 120, 45, 200]
for total in order_totals:
    
    if total > 100:
        print('VIP customers', total)
    else:
        print('Regular customers', total)
        
#               #------enumerate()------#

# enumerate() is just a tool that takes a pile of items and automatically sticks a sequence number
# on every single one of them as it hands them to you. 

# enumerate() gives us both the position/index and the item value while looping.
# Example: index = 0, part = 'LCD'; index = 1, part = 'Battery'; and so on.
# This is useful when you need to know where an item is in the list.

parts = ['LCD', 'Battery', 'Keyboard', 'Trackpad', 'IC', 'CMOS Battery']
for index, part in enumerate(parts):
    print('Part number is', index + 1, part)
    
dishes = ['Burger', 'Pizza', 'Pasta', 'Pancake']
for index, dish in enumerate(dishes):
    print('Task', index + 1, 'Prepare', dish)
  
products = ['Burger', 'Pizza', 'Pasta', 'Pancake', 'Salad']
for product in products:
    print(product)
    if product == 'Pasta':
        break

# Scenario 1

# Imagine you are a manager at the restaurant . You have a list of table orders, but some are
#    marked as "High Priority" because they've been waiting too long.

#        # 1. How do we print "Checking [order]..."?
#        # 2. How do we check if order == priority_table?
#        # 3. If it IS the priority_table, how do we stop the loop immediately?    
orders = ['Table 1', 'Table 2', 'Table 3', 'Table 4']
priority_table = 'Table 3'
    
for order in orders:
    print('Checking:', order)
    if order == priority_table:
        print("Urgent prep needed for", order)
        break

# scenario 2 manager with EGO issues :

# Imagine you are a manager at the restaurant again. You have a list of table orders, but some are
# marked as "High Priority" because they've been waiting too long. well idk care coz Table 3 yelled at me

orders = ['Table 1', 'Table 2', 'Table 3', 'Table 4', 'Table 5']
priority_table = 'Table 3'

for order in orders:
    print('Checking:', order)
    if order == priority_table:
        print(order, 'Is our valuable customer so Let him starve for a While 😂')
        continue

# in this scenario when the table reaches table 3 it will skip table 3 and move on to the next tables.

# Note: don't be a scenario 2 manager.

# let's do a "Shift Report".

# I want you to use enumerate() to generate a report that assigns a Ticket Number to each dish,
# but ticket numbers should start at 101.

orders = ['Burger', 'Pizza', 'Pasta', 'Salad', 'Steak']
for index, order in enumerate(orders):
    print('Ticket', index + 101,':', order)
  

#     The Anatomy of range()
#    range() can take up to three numbers: range(start, stop, step)
    
#    *   start: Where you begin (default is 0).
#    *   stop: Where you finish (this is exclusive, meaning it stops before this number).
#    *   step: How much to add each time (default is 1).


#  Restaurant Scenario: The "Inventory Count"
#    Imagine you are doing a weekly inventory count. 
#    You need to check the stock of items every 2 days (perhaps to let the kitchen rest).

for x in range(2, 11, 2):
    print('Inventory check on day:', x)

# Imagine you have a monthly budget report and you only want to look at the even-numbered days.    
for y in range(2, 31, 2):
    print('Report check on day:', y)
    
  # For loops topics covered so far !
    
#    1.  For loop basics (hiring the assistant).
#    2.  break (the emergency exit).
#    3.  continue (the skip button).
#    4.  enumerate() (the sticky-label machine).
#    5. range() for controlling the number of iterations and skipping values using the step.