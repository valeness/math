import csv
import math

data = []
prices = []
qualities = []

with open('datasets/simple.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append((int(row['price']), int(row['quality'])))
        prices.append(int(row['price']))
        qualities.append(int(row['quality']))

# prices    = x
# qualities = y
# Formula for Pearson's r
# r = sigma(xy) / sqrt(sigma(x^2) * sigma(y^2))

def find_correlation(data):
    tmp_sigma_xy = []
    tmp_sigma_x = []
    tmp_sigma_y = []
    for i in data:
        sum_xy = i[0] * i[1]
        x_squared = math.pow(i[0], 2)
        y_squared = math.pow(i[1], 2)

        tmp_sigma_xy.append(sum_xy)
        tmp_sigma_x.append(x_squared)
        tmp_sigma_y.append(y_squared)
    sigma_xy = sum(tmp_sigma_xy)
    sigma_x = sum(tmp_sigma_x)
    sigma_y = sum(tmp_sigma_y)
    r = round(sigma_xy / math.sqrt(sigma_x * sigma_y), 2)
    return r
r = find_correlation(data)
print(r)

# Expected Output
# 0.76
