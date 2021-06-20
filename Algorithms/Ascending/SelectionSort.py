def SelectionSort(arr):

    for i in range(len(arr)-1):
        m = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j

            yield arr

        if m != i:
            arr[i], arr[m] = arr[m], arr[i]

            yield arr