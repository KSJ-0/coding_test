import sys
input = sys.stdin.readline
count = 0

def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


if __name__ == "__main__":
    N = int(input().strip())
    for _ in range(N):
        count = 0
        word = input().strip()
        result = isPalindrome(word)
        print(result, count)