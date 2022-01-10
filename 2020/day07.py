from parse import parse

with open('input') as file:
    lines = file.readlines()

rules = {}

matcher = '{color} bags contain {content}'
for line in lines:
    r = parse(matcher, line)
    # Bags which do not contain other bags will not appear in dict
    if 'no other bags' in r['content']:
        continue
    content = r['content'].split(',')
    items = {}
    for color in content:
        # [4] [clear] [purple] [bags]
        words = color.strip().split(' ') 
        items[' '.join(words[1:3])] = int(words[0])
    rules[r['color']] = items

#Part 01
number = 0
# Find the starting point
# List the bags colour which contain -- 'shiny gold'
bag_colors = [color for color in rules if 'shiny gold' in rules[color].keys()]
checked = []
while bag_colors:
    # Increase number with the colors found
    number += len(set(bag_colors))
    # Mark which colors have been checked
    checked.extend(list(set(bag_colors)))
    next_colors = []
    for color in bag_colors:
        next_colors.extend([bag for bag in rules if color in rules[bag].keys()])
    # Remove from list already checked colors
    bag_colors = [color for color in next_colors if color not in checked]

print(number)

#Part 02
bags = ['shiny gold']
i = 0
while i != len(bags):
    # If bag not in rules, it means it doesn't contain anything
    if bags[i] in rules:
        # Extend the list with how many bags are found to be in it       
        for bag, number in rules[bags[i]].items():
            # 2 red --> [red] [red] 
            bags.extend(number * [bag])
    i += 1

# Don't consider first entry - shiny gold
print(len(bags[1:]))

# Alternative solution for Part 02 - using recursive function
def count_bags(bag):
    if bag not in rules:
        return 1
    return 1+sum([number * count_bags(color) for color, number in rules[bag].items()])

print(count_bags('shiny gold')-1)