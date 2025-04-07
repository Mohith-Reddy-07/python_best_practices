# Create a DF list
import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ['student_id', 'age'])

 # Example input
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

# Create DataFrame and display it
df = createDataframe(student_data)
print(df)

# Get the size of the DF
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

# Sample DataFrame
data = [
    [846, "Mason", 21, "Forward", "RealMadrid"],
    [749, "Riley", 30, "Winger", "Barcelona"],
    [155, "Bob", 28, "Striker", "ManchesterUnited"],
    [583, "Isabella", 32, "Goalkeeper", "Liverpool"],
    [388, "Zachary", 24, "Midfielder", "BayernMunich"],
    [883, "Ava", 23, "Defender", "Chelsea"],
    [355, "Violet", 18, "Striker", "Juventus"],
    [247, "Thomas", 27, "Striker", "ParisSaint-Germain"],
    [761, "Jack", 33, "Midfielder", "ManchesterCity"],
    [642, "Charlie", 36, "Center-back", "Arsenal"]
]

columns = ['player_id', 'name', 'age', 'position', 'team']
players = pd.DataFrame(data, columns=columns)

# Call the function
print(getDataframeSize(players))