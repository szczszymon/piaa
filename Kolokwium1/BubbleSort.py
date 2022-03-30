def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    ex = [15, 123, -123123, 416, 78, 0, -623, 23]

    print("Pre-Sort array:")
    print(*ex)
    print()

    bubble_sort(ex)

    print("Post-Sort array:")
    print(*ex)
