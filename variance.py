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
