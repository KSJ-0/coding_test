import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = -1
count = 0

def merge_sort(arr, p, r):
    if p<r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    global result, count
    save = 0
    tmp = []
    i = p
    j = q+1
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            save = arr[i]
            tmp.append(save)
            i += 1
            count += 1
            if count==K:
                result = save
        else:
            save = arr[j]
            tmp.append(arr[j])
            j += 1
            count += 1
            if count==K:
                result = save

    while i <= q:
        save = arr[i]
        tmp.append(save)
        i += 1
        count += 1
        if count==K:
            result = save

    while j <= r:
        save = arr[j]
        tmp.append(save)
        j += 1
        count += 1
        if count==K:
            result = save

    for k in range(len(tmp)):
        arr[p+k] = tmp[k]

if __name__ == "__main__":
    merge_sort(arr, 0, len(arr)-1)
    print(result)