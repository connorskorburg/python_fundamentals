arr = [1,5,3,2,0,8]

def selection_sort(arr):
    for x in range(0, len(arr), 1):
        min_pos = x
        for i in range(x + 1, len(arr), 1):
            # print("index:", i, "value", arr[i])
            # print("comparing", arr[i], arr[min_pos])
            if arr[i] < arr[min_pos]:
                arr[i], arr[min_pos] = arr[min_pos], arr[i]
                # print("swapped", arr[i], arr[min_pos])
                # print(arr)
    return arr
print(selection_sort(arr))