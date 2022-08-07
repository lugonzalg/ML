##############APPEND###############

print("APPEND\n")
print("Initial list")
ciudades=["madrid", "barcelona", "sevilla", "valencia"]
print(ciudades)
print("Add elemt to the tail")
ciudades.append("bilbao")
print(ciudades)

##############INSERT###############

print("INSERT\n")
print(ciudades)
print("Add nth elemt")
ciudades.insert(0, "salamanca")
print(ciudades)
print("Add nth elemt")
ciudades.insert(2, "pamplona")
print(ciudades)

#############DEL##############

print("DEL\n")
print(ciudades)
print("delete nth element")
del ciudades[0]
print(ciudades)
print("delete last element")
ciudades.pop()
print(ciudades)
key = "sevilla"
print("delete key element")
ciudades.remove(key)
print(ciudades)
