n = int(input())
arr = list(map(int, input().split()))
target = int(input())

def solution():
    left = 0
    right = n - 1

    while left < right:
        summ = arr[left] + arr[right]

        if summ > target:
            right -= 1
        elif summ < target:
            left += 1
        else:
            return (left, right)   # or (left+1, right+1) for LeetCode

    return -1

ans = solution()
print(ans)
