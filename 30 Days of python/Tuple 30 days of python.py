# Creating a empty Tuple
empty_tuple = ()
print(empty_tuple)

# Tuple with initial values
faaa = ('Violet', 'Vi', "Jinx", 'Ekko')
print(faaa) 
print(len(faaa))

# Accessing Tuple using positive index
fbbb = ("Violet", "Vi", 'Jinx', "Ekko")
name_1 = fbbb[2]
name_2 = fbbb[0]
print(name_1, name_2)

# Accessing Tuple using negachu index
fccc = ("Violet", "Vi", 'Jinx', 'Ekko')
first_name = fccc[-1]
second_name = fccc[-3]
print(first_name, second_name)

# Slicing Tuples
fddd = countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

first_10 = fddd[0:10]
last_10 = fddd[0:3]
print(first_10)
print(last_10)
print(fddd[len(fddd)// 2])
mid = len(fddd) // 2
print(mid)
first_half = fddd[:mid + 1]
print(first_half)

# Slicing Tuples using nega tive index

print(fddd[-3:-1])
print(fddd[-15:-1])
print(fddd[-3:])

# Changing Tuples to lists
feee = ("Violet", 'Vi', "Jinx", 'Ekko') # its a Tuple immutable
temp = list(feee)  # We can change Tuple to list 
temp.insert(4, 'Reze') # After changing the Tuple to list, We can modifiy Tuple
print(feee) # It will print modified Tuple
New_feee = tuple(temp) # After modifing Tuple to List , we can Reverse the process
print(New_feee) # See the Fucking output, Who told you Tuple is immutable!

# Checking an item in Tuple
ffff = ('Violet', 'Vi', 'Jinx', 'Ekko')
print('Jinx' in ffff)
print('Reze' in ffff)

# Joining Tuples 
fggg = ("Violet", 'Vi', 'Jinx', 'Ekko')
fhhh = ('Reze', 'Denji', 'Power', "Aki")
fiii = fggg + fhhh
print(fiii)
print(len(fiii))

# Deleting Tuples del removes the variable name from your
# namespace, not the tuple's contents.




