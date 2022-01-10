class Rule:
    def __init__(self, text):
        # Get name
        self.name = text.split(':')[0]
        # Get ranges
        self.ranges = []
        for part in text.split(':')[1].split('or'):
            self.ranges.append(list(map(int, part.strip().split('-'))))

    def validate(self, value):
        return any([range_[0] <= value <= range_[1] for range_ in self.ranges])


class Ticket:
    def __init__(self, rules, text):
        self.rules = rules
        self.values = list(map(int, text.strip().split(',')))

    def get_invalid_fields(self):
        invalid_values = []
        for value in self.values:
            if not any([rule.validate(value) for rule in self.rules]):
                invalid_values.append(value)
        return invalid_values

    def rules_to_exclude(self, entry_pos):
        to_exclude = []
        for rule in self.rules:
            if not rule.validate(self.values[entry_pos]):
                to_exclude.append(rule.name)
        return to_exclude


with open('input') as file:
    lines = file.readlines()

# Creat rules
rules = []
for line in lines[:20]:
    rules.append(Rule(line))

# My ticket
my_ticket = Ticket(rules, lines[22])

# Scan nearby tickets
nearby_tickets = []
for line in lines[25:]:
    nearby_tickets.append(Ticket(rules, line))

# Error rate
error_rate = 0
# Save indexes of tickets which should be deleted
ticket_to_delete = []
for index, ticket in enumerate(nearby_tickets):
    invalid_fields = ticket.get_invalid_fields()
    if invalid_fields:
        ticket_to_delete.append(index)
    error_rate += sum(invalid_fields)
print(error_rate)

# Delete invalid tickets
for index in sorted(ticket_to_delete, reverse=True):
    del nearby_tickets[index]

possible_rules = {}
for index in range(len(nearby_tickets[0].values)):
    # For all positions generate a list with the name of a rules
    rules_name = [rule.name for rule in rules]
    # For each value find out which rules doesnt apply
    for ticket in nearby_tickets:
        for exclude in ticket.rules_to_exclude(index):
            # Remove the rules from the list
            rules_name.remove(exclude)
    possible_rules[index] = rules_name

rules_location = {}
while possible_rules:
    # Find line with just one entry
    for index, line in possible_rules.items():
        if len(line) == 1:
            known_pos = index
            known_name = line[0]
            # Save rule and location
            rules_location[known_name] = known_pos
            # Remove form the current dict
            del possible_rules[known_pos]
            # Remove this name from all entries
            for index in possible_rules:
                possible_rules[index].remove(known_name)
            break

prod_departure = 1
for name in rules_location:
    if 'departure' in name:
        prod_departure *= my_ticket.values[rules_location[name]]

print(prod_departure)