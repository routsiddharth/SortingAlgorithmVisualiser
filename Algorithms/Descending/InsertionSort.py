def InsertionSort(arr):

    if len(arr) <= 1:
        return arr

    if len(arr) == 2 and arr[1] > arr[0]:
        return arr[::-1]

    else:
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j - 1] < arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1

                yield arr