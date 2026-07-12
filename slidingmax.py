n=int(input())
arr=list(map(int,input().split()))
k=int(input())
def solution():
    l=0
    window=[]
    ans=[]
    maxx=0
    for r in range(n):
        window.append(arr[r])
        size=r-l+1
        if size>k:
            window.remove(arr[l])
            l+=1
            size=r-l+1
        if size==k:
            maxx=window[0]
            for num in window:
                maxx=max(maxx,num)
            ans.append(maxx)

    return ans
            
            
            
            
            
ans = solution()
print(ans)
