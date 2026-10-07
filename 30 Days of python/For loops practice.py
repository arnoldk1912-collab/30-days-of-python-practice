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
    print("The price with 10% tax is:", taxed_price)

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
    print('Part number is', index, part)
    
dishes = ['Burger', 'Pizza', 'Pasta', 'Pancake']
for index, dish in enumerate(dishes):
    print('Task', index + 1, 'Prepare', dish)
  
products = ['Burger', 'Pizza', 'Pasta', 'Pancake', 'Salad']
for product in products:
    print(product)
    if product == 'Pasta':
        break
    