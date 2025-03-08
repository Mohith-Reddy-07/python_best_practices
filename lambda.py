# Lambda furnctions
from functools import reduce

res = (lambda **kwargs: sum(kwargs.values()))
print(res(a = 3, b = 5, c = 7), res(a = 4, b = 6, c = 8))

###############################################

# User defined function to find product of numbers
def product(nums):
    total = 1
    for i in nums:
        total *= i
    return total

res1 = (lambda **kwargs: product(kwargs.values()))
print(res1(a = 3, b = 5, c = 7), res1(a = 4, b = 6, c = 8))

################################################

def myfunc(n):
    return lambda a: a + n

add10 = myfunc(10)
add20 = myfunc(20)

print(add10(5))
print(add20(5))

#################################################

list1 = [1,2,3,4,5,6,7,8,9]

# To filter odd numbers
odd_num = list(filter(lambda n: n%2 == 1, list1))
print(odd_num)

# To filter even numbers
even_num = list(filter(lambda n: n%2 == 0, list1))
print(even_num)

# TO double the numbers
double = list(map(lambda n: n*2, list1))
print(double)

# Sum of the all items in the list
sum_all = reduce(lambda a,b: a+b, double)
print(sum_all)

###################################################

list2 = ['one', 'TWO', 'three', 'FOUR']

upper = list(filter(lambda x: x.isupper(), list2))
lower = list(filter(lambda x: x.islower(), list2))

print(upper)
print(lower)

#######################################################

list3 = ['one', '34', 'twenty2', 'four', 'thirty3', '89']

number = list(filter(lambda x: x.isnumeric(), list3))
word = list(filter(lambda x: x.isalpha(), list3))
numword = list(filter(lambda x: x.isalnum(), list3))

print(number)
print(word)
print(numword)

######################################################
