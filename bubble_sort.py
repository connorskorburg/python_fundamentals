arr = [1,5,3,2,0,8]

def bubble_sort(arr):
    for x in range(0, len(arr) - 1, 1):
        for i in range(0, len(arr) - 1 - x, 1):
            # print("index:", i, "value", arr[i])
            # print('comparing values', arr[i], arr[i+1])
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # print('swapped', arr[i], arr[i + 1])
            # else:
                # print('no need to swap', arr[i], arr[i + 1])
    return arr
print(bubble_sort(arr))