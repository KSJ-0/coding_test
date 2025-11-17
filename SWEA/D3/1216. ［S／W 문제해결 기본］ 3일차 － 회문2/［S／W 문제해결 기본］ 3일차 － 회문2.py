def expand(left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

for _ in range(10):
    test_num = int(input().strip())
    test_case = [input().strip() for _ in range(100)]
    #세로 문자열 만들기
    test_case_cols = [''.join(test_case[r][c] for r in range(100)) for c in range(100)]         
    result = 1
    for text in test_case + test_case_cols:
        for j in range(100):
            expanded_result_1 = expand(j, j, text)
            expanded_result_2 = expand(j, j+1, text)
            result = max(expanded_result_1, expanded_result_2, result)
    print(f"#{test_num} {result}") 
