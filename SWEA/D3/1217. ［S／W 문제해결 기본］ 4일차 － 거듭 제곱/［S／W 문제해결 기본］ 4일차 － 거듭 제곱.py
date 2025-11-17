def cal(result, num, cnt):
    result *= num
    cnt -= 1
    if cnt == 0:
        return result
    return cal(result, num, cnt)
    
for _ in range(10):
    test_num = int(input())
    N, M = map(int, input().split())
    result = 1
    value = cal(result, N, M)
    print(f"#{test_num} {value}")
