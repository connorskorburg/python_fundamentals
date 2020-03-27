arr = [15, 100, 5, 0, 25, 50, 20]
# arr = [0, 15, 100, 5, 25, 50, 20] 
# arr = [0, 5, 15, 100, 25, 50, 20] 
# arr = [0, 5, 15, 20, 100, 25, 50] 
# arr = [0, 5, 15, 20, 100, 25, 50] 
# arr = [0, 5, 15, 20, 25, 100, 50] 
# arr = [0, 5, 15, 20, 25, 50, 100] 

def selection_sort(arr):
    # print(arr)
    for i in range(0, len(arr) - 1, 1):
        min_index = i
        # print("i:", min_index)
        for x in range(i + 1, len(arr), 1):
            # print(f"x: {x}, Value: {arr[x]}")
            if arr[x] < arr[min_index]:
                min_index = x
                # print("Minimum:", arr[min_index])
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # print("SWAPPED")
        # print(arr)
    return arr
print(selection_sort(arr))
