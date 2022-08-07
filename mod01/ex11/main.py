import statistics
import random

randList = []
for i in range(100):
    randList.append(random.randint(1, 1000))

#PROMEDIOS
print("Promedios: ")

retval = statistics.mean(randList)
print("MEDIA INT:", retval)

retval = statistics.fmean(randList)
print("MEDIA FLOAT:", retval)

#GEOMETRIC MEAN?
retval = statistics.geometric_mean(randList)
print("MEDIA GEOMETRICA:", retval)

#HARMONIC MEAN?
retval = statistics.harmonic_mean(randList)
print("MEDIA ARMONICA:", retval)

retval = statistics.median(randList)
print("MEDIANA:", retval)

retval = statistics.mode(randList)
print("MODA:", retval)

#MEDIDAS DE DISPERSION
print("Dispersion: ")

res = statistics.pstdev(randList)
print("DESVIACION TIPICA POBLACIONAL:", res)

res = statistics.stdev(randList)
print("DESVIACION TIPICA MUESTRAL:", res)

res = statistics.pvariance(randList)
print("VARIANZA POBLACIONAL:", res)

res = statistics.variance(randList)
print("VARIANZA:", res)
