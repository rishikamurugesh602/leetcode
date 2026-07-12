s=input()
s1=input()
def solution():
    frequency={}
    freq={}
    for ch in s:
        frequency[ch]=frequency.get(ch,0)+1
    window_size=len(s)
    window=[]
    l=0
    for r in range(len(s1)):
        freq[s1[r]]=freq.get(s1[r],0)+1
        size=r-l+1
        if size==window_size:
            if frequency==freq:
                return True
        if size>=window_size:
            freq[s1[l]]-=1
            if freq[s1[l]]==0:
                del freq[s1[l]]
            l+=1
    return False
        
        
            
ans = solution()
print(ans)
