import json

with open('manager_sales.json', 'r') as file:
    data = json.load(file)
total_price = 0
for item in data:
    summa = sum([i['price'] for i in item['cars']])
    if summa > total_price:
        total_price = summa
        name_manager = item['manager']['first_name']
        last_name_manager = item['manager']['last_name']
print(name_manager, last_name_manager, total_price)

######################################################################################################################

import json

file = open('group_people.json', 'r')
data = json.load(file)

for id in data:
    people = id['people']
    k = 0
    for person in people:
        if person['gender'] == 'Female' and person['year'] >= 1977:
            k += 1
    print(id['id_group'], k)

######################################################################################################################

import json
file = open('Alphabet.json', 'r')
f = open('Abracadabra.txt', 'r', encoding='utf-8')
t = json.load(file)
e=f.read()
decoded=[]
for letter in e:
    decoded.append(t.get(letter, letter))
stroka=''.join(decoded)
print(stroka)