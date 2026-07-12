n=int(input())
arr=list(map(int,input().split()))
k=int(input())
def solution():
    count={}
    for num in arr:
        count[num]=count.get(num,0)+1
    ans=sorted(count.items(),key=lambda x: x[1],reverse=True)
    return ans[:k][0]
    
    
         
anss=solution()
print(anss)
        

    
        
            
