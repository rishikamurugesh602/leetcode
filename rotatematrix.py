m,n=map(int,input().split())
matrix=[]
for _ in range(m):
    row=list(map(int,input().split()))
    matrix.append(row)
def solution():
    row=len(matrix)
    col=len(matrix[0])
    for i in range(row):
        for j in range(i+1,col):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
  
    for row in matrix:
        row.reverse()
    return matrix
ans=solution()
print(ans) 
