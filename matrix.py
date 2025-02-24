def rotate(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for row in matrix:
        row.reverse()
        
n = int(input("enter the range of the matrix(n x n): "))
print(f"enter the {n} x {n} matrix row by row: ")

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    
print("\noriginal matrix: ")
for row in matrix:
    print(row)
    
rotate(matrix)

print("\nrotated matrix: ")
for row in matrix :
    print(row)
    
