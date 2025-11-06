def secret(length, testcases):
    stack = []
    for c in testcases:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return stack

for i in range(1, 11):
    N, testcase = input().split()
    N = int(N)
    length = len(testcase)   

    testcases = [testcase[i] for i in range(length)]


    result = secret(length, testcases)
    password = "".join(result)
    print(f"#{i} {password}")    