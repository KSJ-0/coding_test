#입력이 5일 때 출력
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

num = int(input())
for i in range(num):
    space = num-i-1
    star = 1 + i*2  
    result=" "*space+"*"*star
    print(result)

for i in range(num-1):
    space = i+1
    star = 1 + (num-2-i)*2
    result=" "*space+"*"*star  
    print(result)   