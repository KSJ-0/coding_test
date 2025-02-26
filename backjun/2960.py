# 문제
# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면 다시 2번 단계로 간다.

# 입력
# 첫째 줄에 N과 K가 주어진다.

# 출력
# 첫째 줄에 K번째 지워진 수를 출력한다.

# 풀이 방법
# 0부터 N까지 모든 정수가 적힌 리스트를 생성한다.(리스트의 인덱스와 값을 같게 하기 위해)
# while len(list)==0일 때까지 도는 반복문으로 조건에 맞는 값을 삭제한다.
# 만약 K번째 지워진 수가 존재하면 반복문을 멈추고 출력한다.

#세번째 코드
import sys
N, K = map(int, sys.stdin.readline().strip().split())
check = [True]*(N+1)
count = 0

for i in range(2,N+1): 
    if check[i]:
        for j in range(i, N+1, i):
            if(check[j]==True):
                check[j]=False
                count+=1
            
            if(count==K):
                print(j)
                sys.exit()


#두번째 코드
# import sys
# N, K = map(int, sys.stdin.readline().strip().split())
# check = [True]*(N+1)
# count = 0
# remove_number = 0

# for i in range(2,N+1): 
#     frequency=N//i
    
#     for j in range(1, frequency+1):
#         if check[i*j]==True:
#             remove_number = i*j
#             check[remove_number]=False
#             count+=1
#         if(count==K):
#             print(remove_number)
#             sys.exit()

#처음 코드 remove 사용
# import sys
# N, K = map(int, sys.stdin.readline().strip().split())
# num = [i for i in range(2,N+1)]
# k = 0
# remove_number = 0

# for i in range(2,N+1):
#     if(k==K):
#         break    
#     frequency=N//i
    
#     for j in range(frequency+1):
#         if i*j in num:
#             remove_number = i*j
#             num.remove(remove_number)
#             k+=1
#         if(k==K):
#             break

# print(remove_number)
    