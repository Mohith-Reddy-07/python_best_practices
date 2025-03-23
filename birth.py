def days_together(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    
    def date_to_day_of_year(date: str) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month, day = map(int, date.split('-'))
        return sum(month_days[:month - 1]) + day

    
    arriveAlice = input("Enter Alice's arrival date (MM-DD): ")
    leaveAlice = input("Enter Alice's leave date (MM-DD): ")
    arriveBob = input("Enter Bob's arrival date (MM-DD): ")
    leaveBob = input("Enter Bob's leave date (MM-DD): ")
    
    arriveAliceDay = date_to_day_of_year(arriveAlice)
    leaveAliceDay = date_to_day_of_year(leaveAlice)
    arriveBobDay = date_to_day_of_year(arriveBob)
    leaveBobDay = date_to_day_of_year(leaveBob)
    
    
    start_overlap = max(arriveAliceDay, arriveBobDay)
    end_overlap = min(leaveAliceDay, leaveBobDay)

    
    overlap = max(0, end_overlap - start_overlap + 1)

    return overlap


print(days_together("arriveAlice", "leaveAlice", "arriveBob", "leaveBob")) 
