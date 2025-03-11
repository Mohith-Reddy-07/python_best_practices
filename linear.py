a= '5'
print(int(a))

str1 = "mohith reddy"
print(str1.split(" "))

str2 = "wild animal"
str3 = ""
for i in str2:
    str3 = i + str3
print("original string is: ",str2)
print("reverse string is: ",str3)

l1 = ['cat', 'dog', 'bird']
l1.sort()
print(l1)

print(l1[1])

l1.remove('dog')
print(l1)

l1.pop(1)
print(l1)

l1.clear()
print(l1)

import numpy as np
arr1 = np.array[1, 2, 3, 4]
arr2 = arr1[::-1]
print(arr2)
