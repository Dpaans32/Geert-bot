import random

f = open("Geert.txt", "r")
quotelist = []

for quote in f.readlines():
    quotelist.append(quote.replace('\n', ''))

f.close()

def getRandom(list):
    return random.choice(list)

print(getRandom(quotelist))