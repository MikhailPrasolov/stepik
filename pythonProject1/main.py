import json

file = open('group_people.json', 'r')
data = json.load(file)

# for id in data:
#     people = id['people']
#     k = 0
#     for person in people:
#         if person['gender'] == 'Female' and person['year'] >= 1977:
#             k += 1
#     print(id['id_group'], k)

print(data)
