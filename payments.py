# Display first 3 rows
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# Sample DataFrame
data = [
    [3, "Bob", "Operations", 48675],
    [90, "Alice", "Sales", 11096],
    [9, "Tatiana", "Engineering", 33805],
    [60, "Annabelle", "InformationTechnology", 37678],
    [49, "Jonathan", "HumanResources", 23793],
    [43, "Khaled", "Administration", 40454]
]

columns = ["employee_id", "name", "department", "salary"]
employees = pd.DataFrame(data, columns=columns)

# Apply function
result = selectFirstRows(employees)
print(result)
print("---------------")

# Select Data
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]

# Sample DataFrame
data = [
    [101, "Ulysses", 13],
    [53, "William", 10],
    [128, "Henry", 6],
    [3, "Henry", 11]
]

columns = ["student_id", "name", "age"]
students = pd.DataFrame(data, columns=columns)

# Call the function
result = selectData(students)
print(result)
