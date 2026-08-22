# Exercises: Level 1

empty_tuple = ()
print(empty_tuple)
sisters = ('Violet', 'Vi', 'Jinx', 'Reze')
brothers = ('Ekko', 'Denji', 'Aki', 'Jayce')
print('Sisters Name:', sisters)
print('Brothers Name:', brothers)
siblings = sisters + brothers
print('Siblings:', siblings)
print(len(siblings))
family_members = list(siblings)
family_members.insert(8, 'Vandar')
family_members.insert(9, 'Sreeja')
family_members = tuple(family_members)
print(siblings)
print(family_members)

# Exercises: Level 2

* siblings, ninth, tenth = family_members
print('Siblings:', siblings)
print("Parent\'s:", ninth, tenth)

fruits = ('Apple', 'Mango', 'Banana', 'Orange')
vegetables = ('Carrot', 'Kale', 'Lettuce', 'Endive')
animal_products = ('Milk', "Eggs", 'Honey', "Leather")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
mid = len(food_stuff_lt) // 2
print(food_stuff_lt[mid -1:mid +1])
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
does_exist = 'Estonia' in nordic_countries
print("Does exist:", does_exist)
does_exist = 'Iceland' in nordic_countries
print("Does exist:", does_exist)