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

print('------------------------')
print('-==Data Set==-')
print('------------------------')
print('Relation between price of product and perceived quality')
print('------------------------')
print('(Price, Quality)')
print('------------------------')
print(data)
print('------------------------')

mean_quality = sum(qualities) / len(qualities)
dev_list = []
squared_list = []

# Standard Deviation is the Square Root of the Variance
def find_variance(data, name):
    for k, i in enumerate(data):
        dev = i - mean_quality
        squared_dev = math.pow(dev, 2)
        dev_list.append(dev)
        squared_list.append(squared_dev)
        res = '{index:3} | {quality:2} | {deviation:4} | {squared_deviation:4}'.format(
            index = k,
            quality = i,
            deviation = dev,
            squared_deviation = squared_dev
        )
        print(res)
    mean_deviation = sum(dev_list) / len(dev_list)
    mean_squared = round(sum(squared_list) / len(squared_list), 2)
    final_res = '{spacer:3} | {mean_quality:2} | {mean_deviation:4} | {mean_squared:4}'.format(
        spacer = ' ',
        mean_quality = int(mean_quality),
        mean_deviation = mean_deviation,
        mean_squared = mean_squared
    )
    print('------------------------')
    print(final_res)
    print('------------------------')
    print(' Variance of {} = {}'.format(name, mean_squared))
    print('------------------------')

find_variance(qualities, 'Qualities')
find_variance(prices, 'Prices')

# Expected Output
# ------------------------
# -==Data Set==-
# ------------------------
# Relation between price of product and perceived quality
# ------------------------
# (Price, Quality)
# ------------------------
# [(3, 0), (2, 0), (1, 0), (3, 1), (2, 1), (1, 1), (3, 2), (2, 2), (1, 2), (3, 3), (2, 3), (1, 3), (3, 4), (2, 4), (1, 4)]
# ------------------------
#   0 |  0 | -2.0 |  4.0
#   1 |  0 | -2.0 |  4.0
#   2 |  0 | -2.0 |  4.0
#   3 |  1 | -1.0 |  1.0
#   4 |  1 | -1.0 |  1.0
#   5 |  1 | -1.0 |  1.0
#   6 |  2 |  0.0 |  0.0
#   7 |  2 |  0.0 |  0.0
#   8 |  2 |  0.0 |  0.0
#   9 |  3 |  1.0 |  1.0
#  10 |  3 |  1.0 |  1.0
#  11 |  3 |  1.0 |  1.0
#  12 |  4 |  2.0 |  4.0
#  13 |  4 |  2.0 |  4.0
#  14 |  4 |  2.0 |  4.0
# ------------------------
#     |  2 |  0.0 |  2.0
# ------------------------
#  Variance of Qualities = 2.0
# ------------------------
#   0 |  3 |  1.0 |  1.0
#   1 |  2 |  0.0 |  0.0
#   2 |  1 | -1.0 |  1.0
#   3 |  3 |  1.0 |  1.0
#   4 |  2 |  0.0 |  0.0
#   5 |  1 | -1.0 |  1.0
#   6 |  3 |  1.0 |  1.0
#   7 |  2 |  0.0 |  0.0
#   8 |  1 | -1.0 |  1.0
#   9 |  3 |  1.0 |  1.0
#  10 |  2 |  0.0 |  0.0
#  11 |  1 | -1.0 |  1.0
#  12 |  3 |  1.0 |  1.0
#  13 |  2 |  0.0 |  0.0
#  14 |  1 | -1.0 |  1.0
# ------------------------
#     |  2 |  0.0 | 1.33
# ------------------------
#  Variance of Prices = 1.33
# ------------------------
