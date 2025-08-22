import sys
N = sys.stdin.readline().strip()
cds = list(map(int,sys.stdin.readline().split()))

sorted_cds = sorted(set(cds))

i = 0
dic_cds = {}
for cd in sorted_cds:
    dic_cds[cd] = str(i)
    i += 1

sys.stdout.write(" ".join((dic_cds[cd]) for cd in cds))