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