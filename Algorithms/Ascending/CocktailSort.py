def CocktailSort(arr):

    swapped = True
    start = 0
    end = len(arr) - 1

    while swapped:
        swapped = False

        for i in range(start, end):

            yield arr

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if swapped:
            swapped = False
        else:
            break

        end -= 1

        for i in range(end - 1, start - 1, -1):

            yield arr

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1