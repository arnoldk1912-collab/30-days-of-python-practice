lst = []
print(lst)
faaa = ["Violet", 'Vi', "Jinx", 'Cate', 'Ekko']
print(faaa)
print(len(faaa))
print(faaa[0])
print(faaa[len(faaa)//2])  # Important point
print(faaa[-1])
matrimony_details = ['Kyro', 20, 6.1, 'Single', "Dubai"]
print(matrimony_details)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', "Oracle", 'Amazon']
print(it_companies)
print('Number of companies:', len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies)//2]) # Important point
print(it_companies[-1])
it_companies[-5] = 'Nvidia'
print(it_companies)
it_companies.append('TCS')
print(it_companies)
it_companies.insert(4, 'ASML')
print(it_companies)
it_companies[3] = it_companies[3].upper()
print(it_companies)
result = ' #; '.join(it_companies)
print(result)
does_exist = "ASML" in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
print(it_companies[3:6])
it_companies.pop(0)
print(it_companies)
it_companies.pop(len(it_companies)//2)
print(it_companies)
it_companies.pop(-1)
print(it_companies)
it_companies.clear()
print(it_companies)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
no_end = front_end + back_end
print(no_end)
full_stack = no_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)