import csv
from math import sqrt, pow
import time

data = []
with open('datasets/simple.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append((int(row['price']), int(row['quality'])))

# prices    = x
# qualities = y
# Formula for Pearson's r
# r = sigma(xy) / (sqrt(sigma(x^2) * sigma(y^2)))

def find_correlation(data):
    now = time.time() * 1000
    commands = {'x*y' : [], 'pow(x, 2)' : [], 'pow(y, 2)' : []}
    for (x, y) in data:
        for i in commands:
            calc = eval(i)
            commands[i].append(calc)

    equation = 'round(sum(x*y) / (sqrt(sum(pow(x, 2)) * sum(pow(y, 2)))), 2)'
    for i in commands:
        points = '[{0}]'.format(','.join(str(e) for e in commands[i]))
        equation = equation.replace(i, points)
    r = eval(equation)
    return r

if __name__ == '__main__':
    r = find_correlation(data)
    print(r)
# Expected Output
# 0.76
