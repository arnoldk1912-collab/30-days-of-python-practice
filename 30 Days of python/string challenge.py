name = input("your Full Name : ").split()
result = name[0][0] + name[1][0] + name[2][0]
print(result)

sentence_0 = input("Enter your Sentence: ")
print(sentence_0.lower().count("python"))

sentence_1 = input("Enter your sentence: ")
words = sentence_1.split()
print(" ".join(words[::-1]))

user = input("Your full name: ").split()
name = user[0][0] + user[1][0] + user[2][0]
print(".".join(name))

random = input("Enter your sentence:").istitle()
print(random)

