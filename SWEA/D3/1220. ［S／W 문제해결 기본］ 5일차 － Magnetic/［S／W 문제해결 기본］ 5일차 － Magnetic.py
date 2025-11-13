for i in range(1, 11):
    N = int(input().strip())
    table = [input().split() for _ in range(N)]
    deadlock = 0
    
    for col in range(N):
        one = False
        for row in range(N):
            if "1" == table[row][col]:
                one = True
            elif "2" == table[row][col] and one == True:
                deadlock += 1    
                one = False
                
    print(f"#{i} {deadlock}")