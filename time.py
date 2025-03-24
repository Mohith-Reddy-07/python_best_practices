def countTimes(time: str) -> int:
    count = 1  

    if time[0] == '?':
        if time[1] == '?' or time[1] < '4':
            count *= 3  
        else:
            count *= 2  

    if time[1] == '?':
        if time[0] == '2':
            count *= 4  
        else:
            count *= 10 

    if time[3] == '?':
        count *= 6 

    if time[4] == '?':
        count *= 10

    return count

time = input("Enter the time (hh:mm): ")
print(countTimes(time))
