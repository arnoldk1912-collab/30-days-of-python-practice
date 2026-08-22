# Creating a empty list

lst = list()
print(lst)
empty_list = list()
print(len(empty_list)) # length is 0 coz its fucking empty,Nothing to count

# Using square brackets

lst_1 = []
print(lst_1)
empty_list = []
print(len(empty_list)) # length is 0 coz its fucking empty,Nothing to count

# Creating a list with initial values. and using length len()

fruits = ["Apple", "Orange", "Mango", "Lemon"]
vegie = ["Tomato", "Potato", "Carrot", "Onion"]
city = ["Kovi", "Chennai", "Kochi", "Al ain"]

print("Fruits:", fruits)
print("Number of Fruits:", len(fruits))
print("Veggie:", vegie)
print("Number of veggie:", len(vegie))
print("City\'s:", city )
print("Number of City\'s:", len(city))

# List with different data types

something = ["Kyro", 20, "True", {"Country":"UAE", "City":"Dubai"}]
print(something)

# Accessing list using positive indexing

countries = ["India", "USA", "UAE", "Japan"]
#               0,      1,     2,      3
first_country = countries[0] # India
second_country = countries[1] # USA
thrid_country = countries[2] # UAE
print(first_country, second_country, thrid_country)

# Accessing list using neega indexing

name = ["Alex", "John", "Chriss", "Stan"]
#          -4,    -3,      -2,      -1
first_name = name[-4] # it prints the first name
last_name = name[-1] # it prints the last name
middle_name = name[-2]
print(first_name, last_name, middle_name)

# unpacking list items

lst = ['Item1', 'Item2', 'Item3', 'item4', "Item5"]
first_item, second_item, third_item, *blah, last = lst
print(first_item) # it prints first item
print(second_item) # it prints second item
print(third_item) # it prints third item
print(blah) # it prints rest of the item
print(last) # it prints the last item

# First example
greens = ['Banana', "Leemon", 6, 7, 'manga']
first, second, *rest, last = greens
print(first)
print(second)
print(rest)
print(last)

# 2nd example

fr, se,th, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fr)
print(se)
print(th)
print(rest)
print(tenth)

# Slicing Positive items from a list

fruit = ['Banana', 'Orange', 'Mango', 'Lemon']
all_fruit = fruit[0:4] # It returns all the fruits
all_fruit_1 = fruit[0:] # start from 0 and no value assiend to stop , so prints all fruits
at = fruit[1:3] # starts from index 1 and end befor 3
my = fruit[1:] # start from orange and ends with lemon
leemon = fruit[::2] # it will take every 2nd item
print(all_fruit)
print(all_fruit_1)
print(at)
print(my)
print(leemon)

# Slicing neega tive items from a list

fu = ['Tomato', 'Potato', 'Carrot', 'Cupcake']
#       -4,        -3,       -2,        -1
print(fu[-4:]) # it return's all veegi
print(fu[-3:-1]) # it starts from potato and ends in carrot
print(fu[-3:]) # it starts from potato and end in cupcake
print(fu[::-1]) # it'll fucking revers it

# Modifying lists

faaa = ["Eeny", "Meeny", "Miny", "Moe"]
#         0,       1,      2,      3
faaa[3] = "Meow" # it will modify Index 3 Moe to Meow
print(faaa)
faaa[0] = "Mummy" # it will modify index 0 Eeny ot Mummy
print(faaa)

last_index = len(faaa) -1

# get the index of the last item in the list by -1
# len count total number of item but list is counted by index

faaa[last_index] = "Pookie" 
# replace the last item in the list with 'Pookie'
print(faaa)

# Checking Items in a List

feee = ["Now", "How", "Cow", "Bow"]
does_exist = "Now" in feee # It check's whether [now] is on my list or not
print('Does exist:', does_exist) # if [Now] is there it print True 
does_not_exist = "John wick" in feee
print('Does not exit:', does_not_exist) # if [john wick] is not there it print's False. Got it


# Adding items in a list using append Meth head

fccc = ["Banana", "Monkey", "Cat", 'Booty']
fccc.append('Cutey') # using append we can add new item to the end of a list 
print(fccc)
fccc.append("Poow") # it will add Poow after Cutey 
print(fccc)

# inserting  items on a list using insert Meth Head!

fddd = ['All', 'Ball', 'Call', 'Hall']
#         0,     1,       2,      3   
fddd.insert(3, 'Doll') # insert Doll between Call and Hall
print(fddd)
fddd.insert(4, "Fall")
# Don't wonder where the hell index 4 come from it came when i added Doll got it
print(fddd)

# Removing items from a list using Meth Head!
fggg = ["Banana", "Mine", "Cry", "Nine", "One", "Death"]
fggg.remove("One") # it will remove one,
print(fggg)
fggg.remove("Death") # Death from your life. Die agian stay dead
print(fggg) 

# Removing items using poop Meth Head!
fhhh = ["Violet", "Vi", "Jinx", "Cate", "Ekko", "Jayce"]
# Index    0,      1,     2,      3,      4,       5     
fhhh.pop() # No Index given so it removes the last item.
print(fhhh)
fhhh.pop(0) # It will remove from index {0} violet
print(fhhh)
removed_item = fhhh.pop(2) # Removes the item and returns it removed value
print("Removed Item:", removed_item)

# Removing items using Del keyword
fiii = ["Violet", "Vi", "Powder", "Jinx", "Ekko"]
# Index     0,     1,      2,       3,      4     
del fiii[0] # Delete an item from the list
print(fiii)
del fiii[1:3] # Delete a slice from the list 
print(fiii) 
# Don't get confused seeing the output [Vi, Ekko] before 167 i deleted index zero
# Use your brain not your arse, you dummy!

# clearing list items using Clear Meth Head!
fjjj = ['Violet', 'Vi', 'Powder', 'Jinx', "Ekko"]
fjjj.clear() # Clear removes all items from the list, but keeps variable alive
print(fjjj) # you know what clear dose it clear the list, Fan fucking tastic

# Copying a list

# Example_1 the problem without Copy:
original = ["Violet", "VI", "Jinx"]
fake_copy = original
fake_copy.append("Ekko")

print("Original:", original)
print("Fake Copy:", fake_copy)
# Both changed coz they're pointing at the same list

# Example_2 With copy:
copy_1 = ["Violet", 'Vi', "Jinx"] # Original list
real_copy = copy_1.copy() # i just copyed or dupicate the Original list
real_copy.append("Ekko") # in the copyed list i've added "Ekko"

print(copy_1) # Original list
print(real_copy) 
# Dupicate list with added item [Ekko] without changing original list

# Example_3 Copy then modify freely:
squad = ['Vilot', 'Vi', 'Jinx', 'Ekko']
backup = squad.copy() # i just copyed or dupicate the Original list
squad.clear() # i have cleared original list 

print(squad) # i have wiped original list
print(backup) # Don't worry i have backup plan, I AM BATMAN!

# Joining list
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers) # Joining Negative, zero and positive numbers

# Joining using extend() Methhod!
num_1 = [6, 7, 8, 9, 10]
num_2 = [0, 1, 2, 3, 4, 5]
num_2.extend(num_1) # num_2 will extend with num_1. so the will be [0 to 10]
print(num_2)

negative = [-5, -4, -3, -2,-1]
positive = [1, 2, 3, 4, 5]
zoro = [0]
negative.extend(zoro)
negative.extend(positive) # same as num_1 but different example
print(negative)

# Counting items in a list. Got it sucker
fkkk = ["Violet", "Vi", 'Jinx', "Ekko"]
print(fkkk.count("Jinx")) # it will count how many jinx are there
one = [1, 1, 2, 3, 4, 1, 5, 6, 7, 1, 1, 5, 1, 1, 1, 5, 3, 4, 1, 7, 1, 10, 1, 8]
print(one.count(1)) # it will count 1 in one. simple as fuck

# Finding index of an item. Pov i can find index but not a GF that sucks
flll = ["Violet", 'Vi', 'Jinx', 'Ekko']
print(flll.index("Vi")) # it will find on which index Vi is
fmmm = [1, 1, 2, 3, 4, 1, 5, 6, 7, 1, 1, 5, 1, 1, 1, 5, 3, 4, 1, 7, 1, 10, 5, 8]
print(fmmm.index(10)) # Same using index we can find which index random items located

# Reversing list
flll = ['Violet', 'Vi', 'Jinx', "Ekko"]
flll.reverse() # Reverse() is used when you want to change the list
print(flll)
ages = [22, 19, 14, 11, 13, 14, 34, 99]
print(ages[::-1]) #[::-1] is used when you want reversed copy

# Sorting list items
fnnn = ['Isha', 'Zara', 'Grace', 'Faaa', 'Elza', 'Lisa', 'XXX', 'Akunamatata']
fnnn.sort() # It'll sort the list in Ascending order (A to Z). Faaa!
print(fnnn)
fnnn.sort(reverse=True) # It'll sort the list in descending order (Z to A). Faaa!
print(fnnn)
 
fooo = ['Grace', 'Faaa', 'Elza', 'Lisa', 'XXX', 'Akunamatata']
new_fooo = sorted(fooo) 
#sorted clgives you a new sorted list in ascending order without changing the original list.
print(new_fooo)
print(fooo)
print(sorted(fooo, reverse=True))
# Sorted(reverse=True) gives you new sorted list in descending order 
