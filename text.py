"""from math import log

l = []


with open ("probability.txt", "r") as f:

    for row in f:
        l.append(log(float(row[1])))

print (l)"""
import re
with open('probability.txt') as f:
    num=re.findall('\d*?\.\d+', f.read())
    print(num)