def getUniqueElements(mylist):
    return [el for el in mylist if mylist.count(el) == 1]
mylist = [-1,1,2,2,6,7,7,'say']
print(getUniqueElements(mylist))