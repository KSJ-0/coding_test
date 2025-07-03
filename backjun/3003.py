#문제
#체스는 총 16피스
#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
#흰색 피스의 개수가 주어지면 몇을 +-해야 올바른 세트가 되는지

#입력
#첫째줄에 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수(0<= <=10)

#출력
#몇 개를 +-해야 하는지

import sys
pieces = sys.stdin.readline().strip().split()
correct = [1,1,2,2,2,8]

for i in range(6):
    pieces[i] = correct[i]-int(pieces[i])
    
print(''.join(map(str,pieces)))

#처음 풀아
# import sys
# pieces = sys.stdin.readline().strip().split()
# correct = [1,1,2,2,2,8]
# result = ""

# for i in range(6):
#     if (correct[i]!=int(pieces[i])):
#         if (correct[i]>int(pieces[i])): 
#             result+=str(correct[i]-int(pieces[i]))+" "
#         else:
#             result+="-"+str(int(pieces[i])-correct[i])+" "
#     else:
#         result+="0 "

# print(result)
