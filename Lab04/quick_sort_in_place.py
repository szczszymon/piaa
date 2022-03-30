def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    smaller = []
    eq = []
    bigger = []

    pivot = arr[-1]

    for elem in arr:
        if elem < pivot:
            smaller.append(elem)

        elif elem == pivot:
            eq.append(elem)

        else:
            bigger.append(elem)

    return quick_sort(smaller) + eq + quick_sort(bigger)


if __name__ == "__main__":
    quantity = 6
    lst = []
    inp = "1 15 42 16 82 -40"

    for elem in list(inp.split()):
        lst.append(elem)

    for elem in quick_sort(lst):
        print(f"{elem} ", end="")