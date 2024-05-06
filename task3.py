def productOfAll(mylist):
    result = 1
    for num in mylist:
        result *= num
    return result
mylist=[1,4,5,9,2]
print(productOfAll(mylist))