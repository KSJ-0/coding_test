import sys
N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]
words.sort(key = lambda w: (len(w), w))

before = ""
for word in words:
    if word != before:
        sys.stdout.write(f"{word}\n")
        before = word