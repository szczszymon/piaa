def merge_sort(arr):
    if len(arr) > 1:
        split = len(arr) // 2
        left = arr[:split]
        right = arr[split:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    lst = [76, 11, 3, 54, 6, -516, 1921, -29, 300, 15]
    print("Lista przed sortowaniem:")
    print(lst)
    merge_sort(lst)
    print()
    print("Lista po sortowaniu:")
    print(lst)

