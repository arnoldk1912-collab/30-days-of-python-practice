# If Condition
# In python and other programming languages the key word if is used to check if a condition 
# is true and to execute the block code. Remember the indentation after the colon.

a = 4
if a > 0:
    print('A is Greater')
    
# If Else
# If condition is true the first block will be executed, if not the else condition will run.

b = 3
if b < 0:
    print('B is Negative number')
    
else:
    print("B is positive number")
    
# f Elif Else
# In our daily life, we make decisions on daily basis. We make decisions not by checking one 
# or two conditions but multiple conditions. As similar to life, programming is also full 
# of conditions. We use elif when we have multiple conditions.

c = 0
if c > 0:
    print('C is Positive number')
    
elif c < 0:
    print('C is Negative number')
    
else:
    print('C is Zero')
    
# Short Hand
# value_if_true if condition else value_if_false

d = 5 
print('D is More than') if d > 0 else print('D is less Than')

# Nested Conditions

# Nested conditions Real-world analogy
# Imagine a bouncer at a club checking people at the door:

   # 1. Outer check: "Are you 18 or older?"
# If no → rejected immediately. Doesn't matter what else is true about you.
# If yes → move to the next question (this is where nesting happens)

  # 2.  Inner check (only asked if outer was yes): "Do you have a valid ID?"
# If yes → let them in
# If no → rejected, even though they're old enough

a = 0
if a > 0: #python checks wether a is greater than zero. since a = o, this is a > 0 is false
    if a % 2 == 0: # it's completely skipped
        print('A is positive and even integer')
    else:  # coz the outer if is false, python dosen't even look inside the nested block
        print('A is a positive number')
        
elif a == 0: # Now py checks a ==0. since a actually 0, this is True
    print('A is Zero')
    
else: # This is skipped coz elif matched so py never check the final else chain
    print('A is a negative number')
    
# Nested Conditions workout
age = int(input('Enter your age: '))
day = input('Enter day type (weekend/weekday): ')

if age < 12:
    print('Ticket price: $5')
else:
    if day == 'weekend':
        print('Ticket price: $12')
    else:
        print('Ticket price: $8')
        
order_total = float(input('Enter order total: '))
member = input('Are they a member? (Yes/no): ')

if order_total < 20:
    print('No discount')
else:
    if member == 'Yes':
        print('10% discount applide')
    else: 
        print('5% discount applide')
    

 