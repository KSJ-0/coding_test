import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))   
ops = list(map(int, input().split()))    

max_val = -float('inf')
min_val = float('inf')

def backtrack(idx, current, plus, minus, mul, div):
    global max_val, min_val

    if idx == N:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return

    if plus > 0:
        backtrack(idx+1, current + nums[idx], plus-1, minus, mul, div)

    if minus > 0:
        backtrack(idx+1, current - nums[idx], plus, minus-1, mul, div)

    if mul > 0:
        backtrack(idx+1, current * nums[idx], plus, minus, mul-1, div)

    if div > 0:
        if current < 0:
            backtrack(idx+1, -(-current // nums[idx]), plus, minus, mul, div-1)
        else:
            backtrack(idx+1, current // nums[idx], plus, minus, mul, div-1)


backtrack(1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(max_val)
print(min_val)
