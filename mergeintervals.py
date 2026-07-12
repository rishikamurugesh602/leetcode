n=int(input())
intervals=[]
for _ in range(n):
    start,end=map(int,input().split())
    intervals.append([start,end])
def solution():
    if not intervals:
        return []
    ans=[intervals[0]]
    for i in range(1,n):
        curr_start,curr_end=intervals[i]
        prev_start,prev_end=ans[-1]
        if curr_start<=prev_end:
            ans[-1][1]=max(curr_end,prev_end)
        else:
            ans.append([curr_start,curr_end])
    return ans
anss=solution()
print(anss)
            
    
        
            
