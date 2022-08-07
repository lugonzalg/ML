import math

x = 2.2

res = math.ceil(x)
print("CEIL:", res)

res = math.sqrt(x)
print("SQRT:", res)

res = math.floor(x)
print("FLOOR:", res)

res = math.exp(x)
print("EXP:", res)

res = math.cos(x)
print("COS:", res)

print("PI:", math.pi)

############EXERCISE##########

#1

x = 6.7

res = math.floor(x)
print("FLOOR:", res)

x = -x
res = math.floor(x)
print("FLOOR:", res)

#2

x = -25
try:
    res = math.sqrt(x)
    print("MATH SQRT:", res)
except Exception as e:
    print("MATH:", e)

#3

import cmath

try:
    res = cmath.sqrt(x)
    print("MATH SQRT:", res, "\nTYPE:", type(res))
except Exception as e:
    print("CMATH:", e)


