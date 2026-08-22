# Creating a empty Set
st = set()
print(st)

# Creating a set with initial items
item = {'Item1', 'Item2', 'Item3', 'Item4'}
print(item)

# Getting Set's Length
fruits = {'Banana', 'Orange', 'Mango', 'Lemon'}
print(len(fruits))
fruits_1 = {'Banana', 'Banana', 'Orange', 'Mango', 'Lemon'}
#len         1,          2,        3,       4,        5
print(fruits_1) # it's Unordered and Does not allow duplicates
print(len(fruits_1))
# Even though there are 5 items i will only print 4 because no duplicates allowed

# Accessing Items in a Set
# We use loops to access items. We will see this in loop section

# Checking an Item in set
vegetable = {'Carrot', 'Potato', 'Radish', 'Kale'}
print('Does Vegetable contain Carrot ?', 'Carrot' in vegetable)
print('Does Vegetable contain Mango ?', 'Mango' in vegetable)

# Adding Items to a Set
      # Add one item using add()
names = {'Violet', 'Vi', 'Jinx', 'Ekko'} # Sets are unordered collections.
names.add('Jayce') # They do not preserve insertion order.
print(names) # When you print a set, Python can display the items in any order.

#Add multiple items using update() The update() allows to add multiple items to a set.
# The update() takes a list argument.      
names.update(["Reze", 'Power', 'Aki', 'Denji'])
print(names)

# Removing Items from a Set

colors = {'Black', 'Red', 'Green', 'Blue', 'Yellow', 'Pink'}
colors.remove('Green') # it will remove GREEN from colors set
print(colors)

# Removing set item using pop()
colors.pop() # The pop() methods remove a random item from a list and it returns the removed item.
removed_item = colors.pop() # we can acess removed item in pop method
print(colors)
print("Removed item:", removed_item)

# Clearing Items in a Set
# If we want to clear or empty the set we use clear method.
colors.clear() # it will clear everything from colors set
print(colors)

# Deleting a Set
del colors # If we want to delete the set itself we use del operator.
        

# Remove set using Discard method

colors = {'Red', 'Green', 'Blue'} 

colors.discard('Green') # discard(item) removes an item from the set if it exists.
print(colors)

colors.discard('Yellow') # If the item is not in the set, it does nothing.
print(colors) # Unlike remove(), it does not raise an error.

# Difference between remove() and discard()

# remove() → raises error if item is missing
# discard() → safe, no error if item is missing
# In short, discard() is useful when you want to remove something
# without worrying about whether it exists.

# Converting List to Set
lst = ['item1', 'item2', 'item3', 'item4', 'item1'] # List
lst = set(lst) # Now list is converted to set
print(lst) # Duplicates are removed and the set is displayed in an unordered way

# Joining Sets
# We can join two sets using the union() or update() method or | symbol .

# union() creates a new set and leaves the original unchanged
a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9, 10}
c = a.union(b)
print(a) # Here, a and b stays the same
print(b)
print(c) #  and c is the new combined set.

# Update This method inserts a set into a given set
# update() changes the original set
numbers = {1, 2, 3, 4, 5}
letters = {'A', 'B', 'C', 'D', 'E'}
letters.update(numbers)
print(letters)

fruits_5 = {'banana', 'orange', 'mango', 'lemon'}
vegetables_5 = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits_5 | vegetables_5) # Another union type

# Finding Intersection Items

# Intersection means the common elements between two sets.
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))  # intersection = what is shared by both sets {o, n}

# Symmetric difference: elements in one set or the other, but not both
print(python.symmetric_difference(dragon)) 

# Checking Subset and Super Set
# A subset is a smaller group taken from a bigger group
# A superset is the bigger group that contains the smaller group.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # whole_numbers is a superset of even_numbers
even_numbers = {0, 2, 4, 6, 8, 10,} # even_numbers is a subset of whole_numbers
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

all_students = {'Amina', 'Ben', 'Chris', 'Dina'}
math_students = {'Amina', 'Chris'}

print(math_students.issubset(all_students))     # True
print(all_students.issuperset(math_students))   # True

# both true Because every student in the math group is also in the full student list.

# Checking the Difference Between Two Sets
# difference() removes all items from the first set that also appear in the second set.
# Example: whole_numbers_1 - even_numbers_1 = numbers only in whole_numbers_1.
whole_numbers_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers_1 = {2, 4, 6, 8, 10}
print(whole_numbers_1.difference(even_numbers_1))
print(even_numbers_1.difference(whole_numbers_1))

# x and y are two sets. difference() checks what is only in one set and not the other.
# x.difference(y) shows items in x that are not in y, and y.difference(x) does the opposite.
x = {'Apple', 'Mango', 'Banana', 'Orange', 'Lemon'}
y = {'Orange', 'Grape', 'Melon', 'Apple'}
print(x.difference(y))
print(y.difference(x))

# Joining Sets
# isdisjoint() checks if two sets have no common items.
# If they do share something, the result is False; otherwise it is True.
arcane = {'Violet', 'Vi', 'Jinx', 'Ekko'}
chainsaw_man = {'Reze', 'Denji', 'Aki', 'Makima'}
print(arcane.isdisjoint(chainsaw_man))

number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odd_number = {1, 3, 5, 7, 9}
print(number.isdisjoint(odd_number))