learning = "Thirty Days Of Python"
lesson = "Coding for all"
company = lesson
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find("Coding"))
print(company.replace("Coding", "Python"))

sentence = "Python for everyone"
new_sentence = sentence.replace("everyone", "all")
print(new_sentence)
print(new_sentence.split())

companines = "Facebook, Google, Microsoft, Apple, IBM, Oricle, Amazon"
print(companines.split())
print(company.find("Coding"))
print(len(company) -1)
print(company[10])

words = "Python for everyone".split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)

word = "Coding For All".split()
abbreviation = word[0][:2] + word[1][:3] + word[2][:3]
print(abbreviation)

string = "Coding For All"
print(string.find("C"))
print(string.find("F"))

sentence = "Coding For All people"
print(sentence.rfind("l"))

first_occurrence = 'you cannot end a sentence with because because because is conjunction'
print(first_occurrence.index("because"))
print(first_occurrence.rindex("because"))
print(first_occurrence[31:54])
print(first_occurrence.find('because'))
print(first_occurrence[31:54])
print(first_occurrence.replace("because because because", ""))
print(lesson.startswith("Coding"))
print(lesson.endswith("Coding"))
issue_2 = "  Coding for all   " # hey claude issue 1 and 2 resolved! Happy now
print(issue_2.strip())

print("30daysofpython".isidentifier())
print("thirty_days_of_python".isidentifier())

python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
result = " # ".join(python_libraries)
print(result)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name:\tKyro\nAge:\t14\nCounry:\tUAE\nCity:\tDubai")
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


radius = 10
area = 3.14 * radius ** 2 
print(f"The area of circle with radius {radius} is {int(area)} meters square.")

a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {round(a /b, 2)}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")