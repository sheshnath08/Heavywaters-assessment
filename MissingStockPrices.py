# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import interpolate

n = int(input())

prices = []
for  i in range(0,n):
    price = input().split('\t')[1]
    prices.append(price)

available_prices = []
x = []
missing_index = []

for i in range(len(prices)):
    if "Missing" in prices[i]:
        missing_index.append(i)
    else:
        x.append(i)
        available_prices.append(float(prices[i]))

y = np.array(available_prices)

f = interpolate.UnivariateSpline(x, y, s=3)

for i in missing_index:
    print(f(i))