import sys
input = sys.stdin.readline

S = input().strip()
s_len = len(S)
q = int(input().strip())
dic = {}

for i in range(s_len):
    alpha = S[i]
    if alpha not in dic:
        dic[alpha] = [0]*(s_len+1)
    
    for j in range(i, s_len+1):
        dic[alpha][j] = dic[alpha][i-1] + 1

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)

    if a in dic:
        if l == 0:
            print(dic[a][r])
        else:
            print(dic[a][r]-dic[a][l-1])
    else:
        print(0)