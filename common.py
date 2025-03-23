def common_factors(a: int, b: int) -> int:
    
    factor = min(a,b)
    count = 0
    
    for i in range(1, factor + 1):
        if a % i == 0 and b % i == 0:
            count += 1
    return count
    
n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))

print("common factors: ", common_factors(n1, n2))