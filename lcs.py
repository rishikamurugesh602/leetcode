n=int(input())
arr=list(map(int,input().split()))
def solution():
    a=set(arr)
    longest=0
    for num in a:
        if num-1 not in a:
            curr=num
            count=1
            while curr+1 in a:
                curr+=1
                count+=1
            longest=max(count,longest)
    return longest
ans=solution()
print(ans)
