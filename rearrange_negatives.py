n=int(input())
arr=list(map(int,input().split()))
def solution():
    pos=[]
    neg=[]
    ans=[]
    for i in range(n):
        if arr[i]>0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    for i in range(len(pos)):
        ans.append(pos[i])
        ans.append(neg[i])
    return ans
    
            
ans=solution()
print(ans)
