# 문제
# 첫 세 음만으로 본인이 음을 아는 노래를 맞히는 프로그램을 완성하자.

# 입력
# 첫 번째 줄에 음을 아는 노래의 개수N와 
#     맞히기를 시도할 노래의 개수M이 공백으로 구분되어 주어짐
# 두 번째 줄부터 N줄에 걸쳐 노래 제목의 길이 T와 
#     영어 대소문자로 이루어진 노래 제목 S,
#     해당 노래에 처음 등장하는 일곱개의 음이름이 공백으로 구분되어 주어잠
# N+2번째 줄부터 M개의 줄에 걸쳐 맞히기를 시도할 노래의 첫 세 음이 공백으로 구분되어 주어짐

# 출력
# 입력한 첫 세음으로 시작하는 저장된 노래가 여러 개 있는 경우 : ?
# 입력한 첫 세음에 맞는 저장된 노래가 없는 경우 : !
# 맞는 노래가 한 개인 경우 : 노래 제목

# 풀이 방법
# 첫 번째 줄은 sys.stdin.readline으로 입력받고 N, M에 각각 저장.
# 두 번째 줄부터 sys.stdin.readline으로 입력받고 리스트 songs에 T, S, N을 key로 가지는 딕셔너리로 저장
# N+2번째 줄부터 리스트 quiz에 저장.
# songs를 for문 돌리면서 quiz와 맞는 거 있는지 찾음.
# 변수 result를 선언해놓고 ?인데 다시 저장해야 하는 경우 !로 바꿈.

import sys

N, M = map(int, sys.stdin.readline().strip().split())

songs = {}

for i in range(N):
    song_info = sys.stdin.readline().strip().split()
    S = song_info[1]
    K = song_info[2]+song_info[3]+song_info[4]

    if K not in songs:
        songs[K]=[S]
    else:
        songs[K].append(S)   

for i in range(M):
    sound = sys.stdin.readline().strip().replace(" ","")
    
    if sound in songs.keys():
        if(len(songs[sound])==1):
            print(songs[sound][0])
        elif(len(songs[sound])>=2):
            print("?")
    else:
        print("!")


# 처음 풀이 - 이중 for문 사용
# import sys

# song = sys.stdin.readline().strip().split()
# N = int(song[0])
# M = int(song[1])

# songs = {}
# quiz = []
# K=""

# for i in range(N):
#     song_info = sys.stdin.readline().strip().split()
#     S = song_info[1]
#     K = song_info[2]+song_info[3]+song_info[4]
#     songs[S]=K

# for i in range(M):
#     sound = sys.stdin.readline().strip().replace(" ","")
#     quiz.append(sound)

# for sound in quiz:
#     result="!"
#     for i in songs.keys():
#         if(songs[i]==sound):
#             if(result=="!"): 
#                 result = i
#             elif(result!="!"):
#                 result = "?"
#     print(result)