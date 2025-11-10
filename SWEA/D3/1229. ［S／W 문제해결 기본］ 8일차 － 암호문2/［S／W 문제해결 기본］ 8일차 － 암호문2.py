for i in range(1, 11):
    N = int(input().strip())
    secrets = list(map(int, input().split()))
    M = int(input().strip())
    orders = input().split()

    j = 0
    while j<len(orders):
        if orders[j] == "I":
            x = int(orders[j+1])
            y = int(orders[j+2])
            new_nums = list(map(int, orders[j+3:j+3+y]))
            secrets[x:x] = new_nums
            j += 3 + y
        
        elif orders[j] == "D":
            x = int(orders[j+1])
            y = int(orders[j+2])
            del secrets[x:x+y]
            j += 3
    
    result = " ".join(map(str,secrets[:10]))
    print(f"#{i} {result}")