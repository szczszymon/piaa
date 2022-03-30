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


def heap_extract_max(arr, n):
    if n < 1:
        print("Error: Heap underflow")

    maxi = arr[0]
    print(f"Maxi: {maxi}")
    arr[0] = arr[n-1]
    print(f"Krok: {arr}")
    max_heapify(arr, 0, n-1)
    print(f"Krok: {arr}")
    return maxi


if __name__ == "__main__":
    przyklad = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    n = len(przyklad)

    print(f"Przed: {przyklad}")
    heap_extract_max(przyklad, n)
    print(f"Po: {przyklad}")
