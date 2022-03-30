def max_heapify(arr, x, n):
    l = 2 * x + 1
    r = 2 * x + 2

    if l < n and arr[l] > arr[x]:
        largest = l

    else:
        largest = x

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != x:
        arr[x], arr[largest] = arr[largest], arr[x]
        max_heapify(arr, largest, n)


def build_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)


def heapsort(arr, n):
    build_max_heap(arr, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)


if __name__ == "__main__":
    przyklady = [[1, 3, 1, 2, 7, 9, 1, 6, 1, 0, 4, 2],
                 [15, 3, 99, 1, 25, 7, 9, 9, 1, 100, 6, 1, 0, 12, 4, 2, 9, 0, 87, 122, 54],
                 [0, 12, 4, 2, 9, 0, 87, 122, 54, 1, 2, 11, 55, 99]]

    for przyklad in przyklady:
        n = len(przyklad)

        print("Tablica przed sortowaniem:")
        print(*przyklad)
        print()

        heapsort(przyklad, n)

        print("Tablica po sortowaniu:")
        print(*przyklad)
        print("\n")
