def search_insert(n: list[int], t: int) -> int:
    left, right = 0, len(n) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if n[mid] == t:
            return mid
        elif n[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

n = list(map(int, input("enter list of numbers: ").split(" ")))
t = int(input("enter target number: "))
print(search_insert(n, t))