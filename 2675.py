# 문제
# 문자열 S를 입력받는다.
# 각 문자를 R번 반복해 새 문자열 P를 만든다.
# P를 출력한다.
# S에는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 만 들어갈 수 있다.

# 조건
# 첫째 줄은 테스트 케이스의 개수
# 각 테스트 케이스는 R과 문자열 S가 공백으로 구분됨
# S는 적어도 1이며 20이하이다.

# 문제 풀이 방법
# 1. 테스트 케이스의 개수를 입력받음
# 2. 앞서 입력받은 횟수만큼 테스트 케이스를 입력받는다.
# 3. 입력받은 테스트 케이스를 리스트에 넣는다.
# 4. 반복문으로 새 문자열을 만든다.
# 5. 출력한다.


testNum = int(input())
testList = list()

while testNum>0 :
    testList.append(input())
    testNum-=1

for i in testList :
    P = ""
    length = len(i)
    j=1
    while length>1+j :
        n = int(i[0])
        while n>0 :       
            P = P + i[1+j]
            n-=1
        j+=1
    print(P)