def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    else:
        largest = i

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":
    ex = [17, 0, 0, -1, -6, 23476, -98, 6, 38]

    print("Pre-Sort array:")
    print(*ex)
    print()

    heap_sort(ex)

    print("Post-Sort array:")
    print(*ex)
