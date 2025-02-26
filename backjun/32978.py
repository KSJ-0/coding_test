#요리하는 과정에서 빼먹은 요리 재료를 떠올리자

#입력
# 첫 번째 줄에 파스타를 만들기 위한 요리 재료의 개수 N이 주어짐 (2<=N<=1000)
# 두 번째 줄에 파스타에 들어가는 재료 N가지가 공백으로 구분되어 주어짐(중복 없음)
# 세 번째 줄에 N재료 중 사용한 N-1개의 재료가 공백으로 구분되어 주어짐
# 각 재료는 알파벳 대소문자, 길이 20이하 문자열

#풀이방법
# 모든 재료와 사용한 재료를 각각 리스트에 넣음.
# 리스트를 정렬함.
# 같은 순번에 같은 재료가 있는지 비교.
# 같지 않으면 해당 재료가 빠진 재료임.

import sys
N = int(sys.stdin.readline().strip())
ingredients = sys.stdin.readline().strip().split()
used = sys.stdin.readline().strip().split()

ingredients.sort()
used.sort()
used.append("nothing")

for i in range(N):
    if (ingredients[i]!=used[i]):
        print(ingredients[i])
        break




