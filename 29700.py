# # 문제
# 좌석이 M행 N열의 직사각형 모양으로 배치되어 있는 영화관.
# 이미 예매가 완료된 좌석을 피해 동아리원들이 모두 가로로 이어서 앉을 수 있는 경우의 수를 구하자.

# # 입력
# 첫째 줄
#     - 영화관 세로줄의 개수 N(1<=N<=1000)
#     - 가로줄의 개수 M(1<=M<=5000)
#     - 동아리원의 수 K(1<=K<=10)
# 둘째 줄부터 N개의 줄에 걸쳐 좌석 예매 현황이 길이가 M인 문자열로 주어진다.
# 0은 빈좌석, 1은 예매 불가능한 좌석이다.

# # 출력
# 경우의 수를 출력한다.
# 예매할 수 있는 방법이 없다면 0을 출력한다.

# # 풀이 방법
# 세로줄, 가로줄, 동아리원 수를 각각 저장한다.
# 좌석 예매 현황을 하나의 가로줄을 하나의 문자열로 하여 리스트에 넣는다.
# 좌석 예매 현황 리스트를 for문으로 돌면서 가로줄 길이만큼 다시 for문을 돌며 연속된 0의 개수를 확인한다.
# 연속된 0이 동아리원 수와 같거나 클 때 경우의 수를 +1한다.

import sys

N, M, K = map(int, sys.stdin.readline().strip().split())
seats = []
result = 0

for _ in range(N):
    seats.append(sys.stdin.readline().strip())

for seat in seats:
    check = 0
    for i in range(M):
        if(seat[i]=="0"):
            check+=1
            if(check>=K):
                result+=1
        else: 
            check = 0

print(result)

#처음 코드 - 문자열 슬라이싱 이용
# import sys

# N, M, K = map(int, sys.stdin.readline().strip().split())
# seats = []
# need_seats = ""
# result = 0

# for _ in range(N):
#     seats.append(sys.stdin.readline().strip())

# for _ in range(K):
#     need_seats+="0"

# for seat in seats:
#     for i in range(M):
#         if((i+K)>M): break
#         if(seat[i:(i+K)]==need_seats):
#             result+=1

# print(result)
        