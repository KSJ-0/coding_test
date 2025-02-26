# 문제
# 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

# 예를 들어 순서대로 2,4,5,4,6으로 이루어진 배열이 있을 때 M이 8이고 K가 3이라고 가정하자.
# 특정한 인덱스의 수가 연속해서 세 번까지 더해질 수 있으므로 결과는 6+6+6+5+6+6+6+5인 46이 된다.
# 서로 다른 인덱스에 해당하는 수가 같은 경우엔 다른 것으로 취급한다.

# 큰 수의 법칙 결과를 출력하시오.

# 입력
# 첫째 줄에 배열의 크기 N(1<=N<=1,000)와 M(1<=M<=10,000), K(1<=K<=10,000)이 공백으로 구분되어 주어진다.
# 두번째 줄에 N개의 자연수가 공백으로 구분되어 주어진다. (1<=주어지는 자연수<=10,000)
# K<=M

# 출력
# 큰 수의 법칙 결과

import sys
N, M, K = list(map(int,sys.stdin.readline().split()))
numbers = list(map(int,sys.stdin.readline().split()))

numbers.sort(reverse=True)
biggest = numbers[0]
sec_biggest = numbers[1]

#가장 큰 수가 K만큼 반복해서 더해진 후 그 다음 큰 수가 한 번 더해지는 것을 반복함
#즉 K+1번의 연산이 반복됨
result = (M//(K+1))*(biggest*K+sec_biggest)
if (M%(K+1)!=0): #M이 K+1로 나누어 떨어지지 않는 경우 처리
    result+=(M%K+1)*(biggest)

print(result)

#처음에 작성한 코드
# import sys
# N, M, K = list(map(int,sys.stdin.readline().split()))
# numbers = list(map(int,sys.stdin.readline().split()))

# numbers.sort(reverse=True)
# count = 0
# cur_index = 0
# result = 0

# for _ in range(M):
#     result+=numbers[cur_index]
#     count+=1
#     if (count==K):
#         if (cur_index==0):
#             cur_index=1
#             count=0
#         else:
#             cur_index=0
#             count=0

# print(result)