from collections import deque

for i in range(10):
    N = int(input().strip())
    nums = deque(map(int, input().split()))
    
    j = 0
    while True:
        if j > 4:
            j = 1
        else: j += 1
        
        num = nums.popleft()
        if num - j <= 0:
            num = 0
            nums.append(num)
            break
        else:
            num -= j
            nums.append(num)
                      
    result = " ".join(map(str, nums))        
    print(f"#{N} {result}")

