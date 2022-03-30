import math


def heap_increase_key(arr, i, key):
    i -= 1
    if key < arr[i]:
        print("New key is smaller than current one")
        exit(0)
    arr[i] = key
    while i > 1 and arr[(i - 1) // 2] < arr[i]:
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        print(f"Krok: {arr}")
        i = (i - 1) // 2


def max_heap_insert(arr, key, n):
    arr.append(-math.inf)
    heap_increase_key(arr, n + 1, key)


if __name__ == "__main__":
    przyklad = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    n = len(przyklad)

    print(f"Przed: {przyklad}")
    max_heap_insert(przyklad, 10, n)
    print(f"Po: {przyklad}")
