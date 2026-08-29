dog = {
    'Name' : 'Pug',
     'Color' : 'Black',
      'Breed' : 'Toy breed group',
       'Legs' : 4,
        'Age' : 492,
}
print(dog.items())

student = {
        'First Nmae' : 'Reze',
    'Last Name' : 'Kyro',
        'Gender' : 'Male',
    'Age' : 249, 
        'Marital Status' : 'Single',
    'Skills' : ['Python', 'SQL', 'Power Bi', 'Git'],
        'Country' : 'Ireland',
    'City' : 'Duplin',
        'Address' : {
        'Street' : 'IDK street',
    'Zipcode' : 666
    }
}
print(student)
print(len(student))
print(type(student.get('Skills')))
student['Skills'].extend(['Excel', 'Tabelue'])
print(student)
keys = list(student.keys())
print(keys)
value = list(student.values())
print(value)
print(student.items())
removed_value = student.pop('Marital Status')
print(student)
print("removed value:", removed_value)
student.popitem()
print(student)
del dog
print(dog)
