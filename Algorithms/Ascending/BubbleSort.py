def BubbleSort(arr):

    while not all([arr[j] <= arr[j + 1] for j in range(len(arr) - 1)]):

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

            yield arr