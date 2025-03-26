def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    strs.sort()
    
    first, last = strs[0], strs[-1]
    i = 0
    
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
        
    return first[:i]

strings = input("enter the strings: ").split(" ")
print("longest common string: ", longest_common_prefix(strings))
