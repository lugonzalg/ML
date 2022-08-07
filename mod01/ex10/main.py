import random

x = 1
y = 10

retval = random.randint(x, y)
print(retval)

retval = random.random()
print(retval)

retval = random.uniform(x, y)
print(retval)

choiceList = ["1", "2", "3", "4", "5"]
retval = random.choice(choiceList)
print(retval)

poblacion = ["Madrid", "Barcelona", "Valencia", "Bilbao", "Sevilla", "Zaragoza"]
n = 3
retval = random.sample(poblacion, n)
print(retval)

############################EXERCISE#########################

#MY_CHOICE
bonoList = []
for i in range(1, 50):
    bonoList.append(i)
bonoWinner = random.sample(bonoList, 6)
print(sorted(bonoWinner))

#CURSUS CHOICE
i = 0
bonoWinner = []
while i < 6:
    randNum = random.randint(1, 49)
    if randNum not in bonoWinner:
        bonoWinner.append(randNum)
        i += 1

print(sorted(bonoWinner))
