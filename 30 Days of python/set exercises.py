# Exercises: Level 1

# 1. Find the length of the set it_companies
# 2. Add 'Twitter' to it_companies
# 3. Insert multiple IT companies at once to the set it_companies
# 4. Remove one of the companies from the set it_companies
# 5. What is the difference between remove and discard

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update({'Tcs', 'Infosys', 'Wipro'})
print(it_companies)
removed_item = it_companies.pop()
print(it_companies)
print('Removed item:', removed_item)

# Difference between remove() and discard()

# remove() → raises error if item is missing
# discard() → safe, no error if item is missing
# In short, discard() is useful when you want to remove something
# without worrying about whether it exists.

# Exercises: Level 2

# 1. Join A and B
# 2. Find A intersection B
# 3. Is A subset of B
# 4. Are A and B disjoint sets
# 5. Join A with B and B with A
# 6. What is the symmetric difference between A and B
# 7. Delete the sets completely

A = {19, 22, 24, 20, 25, 26} # Subset
B = {19, 22, 20, 25, 26, 24, 28, 27} # Superset
c = A.union(B)
print(c)
print(A.issubset(B))
print(B.issubset(A))
print(B.issuperset(A))
print(A.issuperset(B))
print(A.isdisjoint(B)) # False because both set has common items
d = B.union(A)
print(d)
# Symmetric difference shows items that are in either set, but not in both.
print(A^B) # # Symmetric difference shows the items that are only in one set: 27 and 28

del A, B
print() 
# # i won't print A, B below (del A, B) because it will rise an error. like A, B is not defined

# Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# 2. Explain the difference between the following data types: string, list, tuple and set
# 3. I am a teacher and I love to inspire and teach people. How many unique words have been 
# used in the sentence? Use the split methods and set to get the unique words.

age = [22, 19, 24, 25, 26, 24, 25, 24]
st = set(age)
print(len(age))
print(len(st))

# 2. Difference between data types
# string: an ordered collection of characters, immutable, enclosed in quotes.
# list: an ordered, mutable collection, written with square brackets []
# tuple: an ordered, immutable collection, written with parentheses ()
# set: an unordered collection of unique values and mutable, written with curly braces {}

sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
unique_words = set(words)
print(unique_words)
print(len(unique_words))