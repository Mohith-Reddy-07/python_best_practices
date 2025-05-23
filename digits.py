def plus_one(digits: list[int]) -> list[int]:
    n = len(digits)
    
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

digits = list(map(int,input("enter the digits: ").split(" ")))
print("re-arranged digits: ", plus_one(digits))
