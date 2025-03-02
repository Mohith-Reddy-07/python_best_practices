def num_duplicate(n: list[int]) -> int:
    
    k = 0
    
    for i in range(1, len(n)):
        if n[i] != n[k]:
            k += 1
            n[k] = n[i]
            
    return k + 1

n = list(map(int,input("enter the numbers: ").split(" ")))
d = num_duplicate(n)
print("Number of unique elements:", d)
print("Modified array:", n[:d])
