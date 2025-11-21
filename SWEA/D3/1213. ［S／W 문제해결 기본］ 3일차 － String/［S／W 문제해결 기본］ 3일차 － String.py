for i in range(10):
    testNum = input().strip()
    findSen = input().strip()
    sentence = input().strip()
    
    cnt = 0
    start = 0

    while True:
        idx = sentence.find(findSen, start)
        if idx == -1:
            break
        cnt += 1
        start = idx + 1
    print(f"#{testNum} {cnt}")