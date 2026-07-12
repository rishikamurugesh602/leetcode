A=input()
k=int(input())
def solution():
    hashmap={}
    
    left=0
    ans=0
    max_freq=0
    for r in range(len(A)):
        hashmap[A[r]]=hashmap.get(A[r],0)+1
        max_freq = max(max_freq, hashmap[A[r]])
        window_size=r-left+1
        requirements=window_size-max_freq
        if requirements>k:
            hashmap[A[left]]-=1
            left+=1
        ans=max(ans,r-left+1)
    
    return ans
        
            
ans = solution()
print(ans)
