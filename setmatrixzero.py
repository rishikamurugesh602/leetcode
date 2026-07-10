m,n=map(int,input().split())
matrix=[]
for _ in range(m):
    row=list(map(int,input().split()))
    matrix.append(row)
def solution():
    row=len(matrix)
    cols=len(matrix[0])
    seen=[]
    for i in range(row):
        for j in range(cols):
            if matrix[i][j]==0:
                seen.append((i,j))
    for r,c in seen:
        for j in range(cols):
            matrix[r][j]=0
        for i in range(row):
            matrix[i][c]=0
    return matrix
            
ans=solution()
print(ans)
