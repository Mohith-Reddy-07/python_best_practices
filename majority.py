from collections import Counter

def majority_number(n: list[int]) -> int:
    count = Counter(n)
    
    for i in count:
        if count[i] > len(n) // 2:
            return i
        
n = list(map(int, input("enter list of numbers: ").split(" ")))
print(majority_number(n))