# 1) single line string

first_name = "Arnold"
last_name = "Kyro"
space = " "
full_name = first_name + space + last_name
print(f"My full name is {full_name}!")

first_name = ":"
print(first_name.upper())
print(first_name.lower())
print(len(first_name))

# 2) multi-line string
message = '''Hello,
my name is Arnold. 
nice to meet you!'''
print(message)

# 3) f-string
price = 5
quantity = 3
print(f"I brought {quantity} items for a total of ${price * quantity}")

# 4) String methoods 

messy = "   Hello arnold!    "
print(messy.strip())
print(messy.upper())
print(messy.lower())
print(messy.title())
print(messy.split())
print(messy.find("o"))
print(messy.count("l"))
print(messy.startswith(" "))
print(messy.endswith(" "))
print(messy.replace("arnold", "kyro"))
print(messy.capitalize())

# String indexing & slicing

name = 'Arnold'

#[A, r, n, o, l, d] for reference
#[0, 1, 2, 3, 4, 5] {Positive index}
#[-6,-5,-4,-3,-2,-1] {Negative index}

first_letter = name[0]
last_letter = name[-1]
print(first_letter, last_letter)
print(name[1:4]) # start from [r:1] to [n:2]
print(name[:4]) # it start from the beginning
print(name[2:]) # start from [n:2] to [d:5]
print(name[:]) # skip this one it's bullshit insted just print(name)
print(name[-3:]) # start from [o:-3] to [d:-1]
print(name[::2]) # skip 1 letter if it is [::3] skip 2 letter
print(name[::-1]) # it fucking reverse the string

# Skipping character while splitting Python strings

lanuguage = "python"
pto = lanuguage[0:6:2] # [Start:End:Step]
print(pto)

#  [0] start index  
#  [6] stop befor 6
#  [2] take every 2nd character 

# Escape sequence

print("hello \n world") # \n New line
print("Nmae:\tArnold")
print("Age:\t22")       # \t New tab
print("city:\tAl Ain")
print("Name:Arnold\t Age:22\t city:Al ain")
print("name:\\Arnold")
print("Hi claude i\'m Arnold") # single or double quote (',") inside string

don = "Aramaki"
print(don.swapcase()) # Uppercase letter become lowercase and lowercase become uppercase

# Acronym

#[0][0] means Give me the first letter of first word

words = "Python for everyone".split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym) 

# index by words

# Words[0] = "python"
# Words[1] = "for"
# Words[2] = "Everyone"

# index by letter

# words[0][0] = "Python"[o] = "p"
# words[1][0] = "for"[0] = "f"
# Words[2][0] = "everyone"[0] "e"

# Abbrevation

word = "Coding For All".split()
abbreviation = word[0][:2] + word[1][:3] + word[2][:3]
print(abbreviation)

# index by word

# word[0] = "coding"
# word[1] = "for"
# word[2] = "all"

#index by letter

# word[0][:2] = "coding"[:2] = "co" cut's everytthing from index 2
# word[1][:3] = "for"[:3] = "for" [if it is [:2] insted of "for", it will become "f0"]
# word[2][:3] + "all"[:3] = "all" [same as line 117]

# R Methods

x = "Milkshake For All People"
print(x.find("l")) # it finds the first l starting from left
print(x.rfind("l")) # it finds the last l starting from right
print(x.index("l")) # same as .find("l")
print(x.rindex("l")) # same as .rfind("l")
print(x.split(" ", 1)) # it split off the first word ("Milkshake")
print(x.rsplit(" ", 1)) # it leaves first three word and split off the last word ("People")

# Remove prefix and suffix

text = "Hello Kyro, how are you" 

print(text.removeprefix("Hello")) # so prefix means beginning part it could be "He"
print(text.removesuffix("you")) # so suffix means ending part it could be "yo"

# String join()

separator = ["A", "B", "C", "D"]
# A join() is like a magic string that glues a bunch of little words

result = "".join(separator)
print(result)
result = " ".join(separator)
print(result)
result = ",".join(separator)
print(result)
result = " # ".join(separator)
print(result)

# import math for calculation

import math

radius = 10
area = math.pi * radius ** 2 
print(f"The area of circle with radius {radius} is {area} meters square.")

# Checks whther it title or not and prints True or false

random = input("Enter your sentence:").istitle()
print(random)