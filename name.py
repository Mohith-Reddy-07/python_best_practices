def people_height(names: list[str], heights: list[int]) -> list[str]:
    people = list(zip(names, heights))
    
    people.sort(key=lambda x: x[1], reverse=True )
    
    return[person[0] for person in people]
    
names = input("enter the names of the people: ").split(" ")
heights = list(map(int,input("enter the heights of the people: ").split(" ")))
print(people_height(names, heights))