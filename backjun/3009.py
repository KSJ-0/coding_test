import sys

a, b = list(map(int,sys.stdin.readline().split()))
c, d = list(map(int,sys.stdin.readline().split()))
e, f = list(map(int,sys.stdin.readline().split()))

x_list = [a,c,e]
y_list = [b,d,f]

x = 0
y = 0

for i in x_list:
    num_count = x_list.count(i)
    if num_count==1:
        x = i
        break

for i in y_list:
    num_count = y_list.count(i)
    if num_count==1:
        y = i  
        break

print("%d %d" %(x,y))
    