for i in range(1, 11):
    N = int(input().strip())
    table = [input().split() for _ in range(N)]
    deadlock = 0
    before = ""
    for n in range(N):
        one = False
        for m in range(N):
            if "1" == table[m][n]:
                one = True
                before = "1"
            elif "2" == table[m][n] and one == True:
                if before is not "2":
                    deadlock += 1    
                before = "2"
    print(f"#{i} {deadlock}")    
