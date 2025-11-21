for i in range(10):
    testNum = input().strip()
    findSen = input().strip()
    sentence = input().strip()
    cnt = 0
    for j in range(len(sentence)):
        sen = sentence[j:j+len(findSen)]
        if sen == findSen:
            cnt += 1
    print(f"#{testNum} {cnt}")