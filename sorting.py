def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

sample_list = [5, 2, 8, 1, 3]
print("Input:", sample_list)
sorted_list = bubble_sort(sample_list)
print("Output:", sorted_list)