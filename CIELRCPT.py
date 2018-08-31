arr = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
for _ in range(int(input())):
    menus, i = 0, 0
    price = int(input())

    while price != 0 and i <= len(arr):
        if price < arr[i]:
            i += 1
        else:
            price = price - arr[i]
            menus += 1

    print(menus)
