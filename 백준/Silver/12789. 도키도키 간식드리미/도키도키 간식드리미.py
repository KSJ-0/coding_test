import sys
N = int(sys.stdin.readline().strip())
now = list(map(int, sys.stdin.readline().split()))
wait = []

i = 1
while now or wait:
    if now and now[0] == i :
        now.pop(0)
        i += 1
    elif wait and wait[-1] == i :
        wait.pop()
        i += 1
    elif now:
        wait.append(now.pop(0))
    else:
        break

if not now and not wait:
    print("Nice")  
else:
    print("Sad")