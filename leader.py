n=int(input())
arr=list(map(int,input().split()))
def solution():
  ans=[]
  max_so_far=arr[n-1]
  for i in range(n-1,-1,-1):
      if arr[i]>=max_so_far:
          max_so_far=max(arr[i],max_so_far)
          ans.append(max_so_far)
  ans.reverse()
  return ans
         
          

    
    
    
        
        
        
    
ans=solution()
print(ans)
