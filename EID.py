for _ in range(int(input())):
    no = int(input())
    arr = sorted(list(map(int, input().split())))
    mini = 999999999
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < mini:
            mini = abs(arr[i] - arr[i+1])
    print(mini)
