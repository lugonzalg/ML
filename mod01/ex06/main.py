#############DICT###########

notas = {}
notas["Matematica"] = 5
notas["Economia"] = 6
notas["Informatica"] = 7
notas["Fisica"] = 8

print("PRE-DELETE:", notas)
del notas["Matematica"]
print("POST-DELETE:", notas)
print(notas.get("Filosofia", "Materia inexistente"))
print(notas.get("Informatica", "Materia inexistente"))
