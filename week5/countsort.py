def count_Sort(arr):
    size = len(arr)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


arr = [7,1,2,1,4,2,3,1,2,3,2]
count_Sort(arr)

print(arr)