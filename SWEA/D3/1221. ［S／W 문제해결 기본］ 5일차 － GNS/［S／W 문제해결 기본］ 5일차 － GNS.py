N = int(input().strip())
c = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(N):
    dic = {c[i]:0 for i in range(10)}
    case_num, cnt = input().split()
    words = input().split()

    for word in words:
        dic[word] += 1
        
    result = []
    for word in c:
        result.append((word + " ")*dic[word])
    print(case_num)
    print(" ".join(result))
        