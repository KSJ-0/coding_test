# 문제
# 입력으로 받은 붕어빵이 좌우로 뒤집힌 모양을 출력한다.

# 조건 
# 1. 첫째 줄에는 두 개의 정수 N, M이 주어진다(0<=N,M<=10)
# 2. 둘째 줄부터 N개의 줄에 걸쳐 붕어빵의 모양이 주어진다.
# 3. 공백은 0, 붕어빵은 1로 표시한다.
# 4. 0과 1은 총 M개이다.

# 문제 풀이
# 1. 입력 첫째 줄의 두 개의 정수 N, M을 변수에 저장한다.
# 2. N번 반복하는 반복문으로 붕어빵 모양을 리스트에 저장한다.
# 3. 리스트를 도는 반복문으로 각 요소의 맨 뒤부터 처음까지 출력한다.

fish = input()
fish = fish.split()
N = int(fish[0]) #1
M = int(fish[1])

n = N
fish_list = list()
while n>0 : #2
    fish_list.append(input())
    n-=1

for i in fish_list : #3
    length = M - 1
    fish_back = ""
    while length>=0 :
        fish_back+=i[length]
        length-=1
    print(fish_back)    
