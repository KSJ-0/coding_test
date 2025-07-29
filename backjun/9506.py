import sys

while True:
    n = int(sys.stdin.readline().strip())
    
    if n==-1:
        break
    
    num_list = []
    
    for i in range(1,n):
        if(n%i==0):
            num_list.append(i)

    total = 0
    
    for i in num_list:
        total += i
    
    if (total==n):
        result=""
        for i in num_list:
            result = " + ".join(map(str,num_list))
        print("%d = %s" %(n,result))

    else:
        print("%d is NOT perfect." %n)