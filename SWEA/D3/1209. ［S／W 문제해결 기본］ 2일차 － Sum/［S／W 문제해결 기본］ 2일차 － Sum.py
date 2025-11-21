for _ in range(10):
    testNum = input().strip()
    numArr = [list(map(int, input().split())) for _ in range(100)]
    
    #행의 합
    maximum = 0
    for arr in numArr:
        maximum = max(maximum, sum(arr))

    #열의 합
    numArrRe = [sum([numArr[j][i] for j in range(100)]) for i in range(100)]
    maximum = max(maximum, max(numArrRe))

    #대각선의 합
    crossR = [numArr[l][l] for l in range(100)]
    maximum = max(maximum, sum(crossR))
    crossL = [numArr[k][100-1-k] for k in range(100)]
    maximum = max(maximum, sum(crossL))
    
    print(f"#{testNum} {maximum}")