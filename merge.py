def merge(n1: list[int], n2: list[int]) -> list[int]:
    
    m = len([num for num in n1 if num != 0])
    n = len([num for num in n2 if num != 0])
    
    
    i, j, k = m - 1, n - 1, m + n - 1
    
    while i >= 0 and j >= 0:
        if n1[i] > n2[j]:
            n1[k] = n1[i]
            i -= 1
        else:
            n1[k] = n2[j]
            j -= 1
        k -= 1  

    while j >= 0:
        n1[k] = n2[j]
        j -= 1
        k -= 1
    
    return n1  

n1 = list(map(int, input("Enter first array (with extra zeros): ").split()))
n2 = list(map(int, input("Enter second array: ").split()))

result = merge(n1, n2)
print("Merged array:", result)