with open('input') as file:
    data = file.read().split('\n\n')

#Part 01
print(sum([len(set(group.replace('\n', ''))) for group in data]))

#Part 02
same_answers = 0
for group in data:
    persons = group.split('\n')
    for answer in persons[0]:
        same_answers += all([answer in person for person in persons])
print(same_answers)