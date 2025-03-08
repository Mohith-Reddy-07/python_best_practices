from collections import Counter

def mostEven(nums: list[int]) -> int:
    evens = [num for num in nums if num % 2 == 0]
    
    if not evens:
        return -1
    
    count = Counter(evens)
    
    return min(count, key=lambda x: (-count[x], x))

nums = list(map(int, input("Enter numbers: ").split(" ")))
print(mostEven(nums))
