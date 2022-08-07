################SET##############

mySet = {1,2,3,4,5,5,1}
print(type(mySet))
print(mySet)
try:
    mySet =  {[1,2],[2,3],[1,2]}
    print("SET:", mySet(mySet))
    print(mySet)
except Exception as e:
    print(e)
mySet =  {(1,2),(2,3),(1,2)}
print(mySet)

goodSet = set([1,1,2,3,4,5,6])
print(goodSet)
