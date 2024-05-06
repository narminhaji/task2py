def IsSquare(num):
    min, max = 0, num
    while (min <= max):
        mid = int((min + max) / 2)
        if (mid * mid < num):
            min = mid + 1
        elif (mid * mid > num):
            max = mid - 1
        else:
            return True
    return False
mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
squares = list(filter(IsSquare, mylist))
print(squares)