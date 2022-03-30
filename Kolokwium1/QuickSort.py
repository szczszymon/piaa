def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    ex = [23, -37, 74, 0, 9, 9, -7, -6, 4, 123]

    print("Pre-Sort array:")
    print(*ex)
    print()

    quick_sort(ex, 0, len(ex) - 1)

    print("Post-Sort array:")
    print(*ex)