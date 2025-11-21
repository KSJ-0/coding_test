for _ in range(10):
    testNum = input().strip()
    numArr = [list(map(int, input().split())) for _ in range(100)]
    
    #행의 합
    maximum = 0
    for arr in numArr:
        maximum = max(maximum, sum(arr))

    #열의 합
    numArrRe = [[numArr[j][i] for j in range(100)] for i in range(100)]
    for arrRe in numArrRe:
        maximum = max(maximum, sum(arrRe))

    #대각선의 합
    crossR = [numArr[l][l] for l in range(100)]
    maximum = max(maximum, sum(crossR))
    crossL = [numArr[100-1-k][k] for k in range(100)]
    maximum = max(maximum, sum(crossL))
    
    print(f"#{testNum} {maximum}")