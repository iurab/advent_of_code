import re

with open('input') as file:
    text = file.readlines()

def do_math_01(expression):
    while r := re.search(r'[0-9]+(\+|\*)[0-9]+', expression):
        expression = expression.replace(r[0], str(eval(r[0])), 1)
    return expression

def do_math_02(expression):
    for match in re.findall(r'[0-9\+]{3,}', expression):
        expression = expression.replace(match,str(eval(match)), 1)
    return str(eval(expression))

results = []
for line in text:
    homework = '(' + line.strip().replace(' ', '') + ')'
    # Search for ( ) where the calculation can be done already
    while r := re.search(r'\([0-9\+\*]+\)', homework):
        result = do_math_01(r[0][1:-1])
        homework = homework.replace(r[0], result)
    results.append(int(homework))
print(sum(results))
