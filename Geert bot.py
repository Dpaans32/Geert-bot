f = open("Geert.txt", "r")
quotelist = []

for quote in f.readlines():
    quotelist.append(quote.replace('\n', 'n'))

f.close()

print(quotelist)