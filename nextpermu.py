n=int(input())
arr=list(map(int,input().split()))
def solution():
    i=n-2
    second=0
    pivot=-1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot=i
            break
    if pivot==-1:
        arr.reverse()
        return arr
    for i in range(n-1,pivot,-1):
        if arr[i]>arr[pivot]:
            minn=i
            break
    arr[pivot],arr[minn]=arr[minn],arr[pivot]
    left=pivot+1
    right=n-1
    while left<=right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
    
    
    
        
        
        
    
ans=solution()
print(ans)
