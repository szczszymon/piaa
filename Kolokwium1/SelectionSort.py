def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_id = i
        for j in range(i + 1, n):
            if arr[min_id] > arr[j]:
                min_id = j

        arr[i], arr[min_id] = arr[min_id], arr[i]


if __name__ == "__main__":
    ex = [123, 453, -234, 34, 0, 1, 1, 78]

    print("Pre-Sort array:")
    print(*ex)
    print()

    selection_sort(ex)

    print("Post-Sort array:")
    print(*ex)
