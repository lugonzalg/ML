import statistics
import random

randList = []
for i in range(1000000):
    randList.append(random.randint(1, 1000))

retval = statistics.mean(randList)
print(retval)

retval = statistics.geometric_mean(randList)
print(retval)

retval = statistics.harmonic_mean(randList)
print(retval)

retval = statistics.median(randList)
print(retval)

retval = statistics.mode(randList)
print(retval)
