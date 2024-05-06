num1 = [1, 2, 3]
num2 = [4, 5, 6]
length = min(len(num1), len(num2))
result = []
for i in range(length):
    avg = (num1[i] + num2[i]) / 2
    result.append(avg)
print(result)