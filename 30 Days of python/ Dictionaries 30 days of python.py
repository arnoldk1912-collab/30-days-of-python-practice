# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
# To create a dictionary we use curly brackets, {} or the dict() built-in function.

# Creating a empty distionary
empty_dict = {}
print(empty_dict)

# Dictionary with data values
info = {
    "Name" : 'Kyro', # # "Name" is the KEY, 'Kyro' is the VALUE
     "Age" : 666,
       'Country' : 'UAE',
         'City' : 'Dubai',
          'is_single' : True,
             'Address' : {
          'street' : 'Sky street',
        'Zipcode' : 666
    }
}

print(info)
# Dictionary Length checks the number of 'key: value' pairs in the dictionary.
print(len(info)) 
# Accessing Dictionary Items
print(info['Name'])
print(info['Address'])
print(info['Country'])
print(info['is_single'])

# Accessing an item by key name raises an error if the key does not exist. 
# To avoid this error first we have to check if a key exist or we can use the get method. 
# The get method returns None, which is a NoneType object data type, if the key does not exist.
print(info.get('Name'))
print(info.get('Skills')) #insted of key error it will print none. coz we dont have skill in info

# Adding Items to a Dictionary
info['Skills'] = ['Python', 'SQL', 'Excel', 'Power bi']
print(info)
info['Skills'].append('Git')
print(info)
info['languages'] = ['Tamil']
print(info) 
info['languages'].extend(['Hindi', 'English', 'French', 'spanish'])
print(info) # extend() adds multiple items to a list

# Modifying Items in a Dictionary
info['Name'] = 'Arnold'
info['Age'] = 777
print(info)

# Checking Keys in a Dictionary
# We use the in operator to check if a key exist in a dictionary
print('Name' in info)
print('Movies' in info)

# Removing Key and Value Pairs from a Dictionary

# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

Removed_value = info.pop('Name')
print(info)# # Removes the name item
print('Removed value:', Removed_value) # pop() returns the removed value, so we can print it
info.popitem()
print(info) # Removes the languages item
del info['is_single']
print(info) # Removes the is_single item

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.

dct =         {'key1':'value1',
            'key2':'value2',
        'key3':'value3', 
       'key4':'value4'
     }
print(dct)
print(dct.items())

# Clearing a Dictionary
# If we don't want the items in a dictionary we can clear them using clear() method
dit = {'key1':'value1', 
         'key2':'value2',
           'key3':'value3',
             'key4':'value4'
                            }
print(dit.clear())

# The key difference:
# No colon {} = SET
# With colon key: value = DICTIONARY

# no colon inside {} so Python treats it as a SET containing one tuple (1, 2, 3), NOT a dictionary
d = {
      (
         1,
            2,
         3,
      )
   }
print(d)

# 'e' has a colon -> this IS a dictionary, using the tuple (1,2,3) as the key
e = {(1,2,3): 'Some value'}
print(e)

# The key difference: 
# No colon {} = SET
# With colon key: value = DICTIONARY

# {1, 2, 3} = set
# {(1, 2, 3)} = set containing a tuple
# {(1, 2, 3): "value"} = dictionary with a tuple key

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.

random = {
   'Number\'s' : {
      'Whole numbers' : (0, 1, 3, 4, 5, 6, 7, 8),
       'Odd number\'s' : (1, 3, 5, 7, 9),
         'Even number\'s' : (0, 2, 4, 6, 8),
      },
         'Alphabets\'s' : {
            "Vowels" : ['A', 'E', 'I', 'O', 'U'],
              'Consonants' : ['B', 'C', 'D', 'F', 'G']
             }
         }

print(random)
print(random.items())

# Copy a Dictionary
# We can copy a dictionary using a copy() method.
# Using copy we can avoid mutation of the original dictionary.

random_copy = random.copy()  # creates a separate copy of the dictionary
random_copy['Skills'] = ['Python']  # adds a list value to the copied dictionary
random_copy['Skills'].append('sql')  # adds one item to the list
random_copy['Skills'].extend(['Excel', 'Power bi', 'Git'])  # adds multiple items to the list
print('Random:', random)  # shows the original dictionary
print('random copy:', random_copy)  # shows the copied dictionary with changes
print(random_copy.clear())  # clears the copied dictionary and prints None

# Getting Dictionary Keys as a List
# The keys() method gives us all the keys of a a dictionary as a list.
keys = random.keys()
print(keys)

# Getting Dictionary Values as a List
# The values method gives us all the values of a a dictionary as a list.
values = random.values()
print(values)