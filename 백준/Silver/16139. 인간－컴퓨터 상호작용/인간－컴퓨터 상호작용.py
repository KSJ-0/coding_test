import sys
input = sys.stdin.readline

S = input().strip()
s_len = len(S)
q = int(input().strip())
dic = {}

for c in range(ord('a'), ord('z')+1):
    dic[int(c)] = [0]*(s_len+1)


for i in range(s_len):
    k = ord(S[i])
    for alpha in dic:
        if alpha == k: 
            dic[alpha][i+1] = dic[alpha][i] + 1
        else:
            dic[alpha][i+1] = dic[alpha][i]

for _ in range(q):
    a, l, r = input().split()
    a = ord(a)
    l = int(l)
    r = int(r)

    if a in dic:
        if l == 0:
            print(dic[a][r+1])
        else:
            print(dic[a][r+1]-dic[a][l])
    else:
        print(0)