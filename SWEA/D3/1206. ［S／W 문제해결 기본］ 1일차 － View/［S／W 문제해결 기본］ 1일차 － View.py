for k in range(10):
    N = int(input().strip())
    buildings = list(map(int, input().split()))
    count = 0

    for i in range(2, N - 2):
        # 현재 건물 기준으로 양옆 두 칸 중 최대 높이 찾기
        max_side = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        
        # 현재 건물이 양옆보다 높을 때만 조망권 발생
        if buildings[i] > max_side:
            count += buildings[i] - max_side

    print(f"#{k+1} {count}")

