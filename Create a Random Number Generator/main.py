import datetime

seed = datetime.datetime.now().microsecond

seed = int(str(seed)[::-1])

if (seed % 2 == 0):
    seed **= seed % 10
else:
    seed *= seed % 50

print(1 / (seed % 100))