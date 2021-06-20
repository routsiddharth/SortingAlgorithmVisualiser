def ShellSort(arr):
    subarrs = len(arr) // 2

    while subarrs > 0:

        for start_position in range(subarrs):
            yield from GISort(arr, start_position, subarrs)

        subarrs //= 2


def GISort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):

        current_value = arr[i]
        position = i

        while position >= gap and arr[position - gap] > current_value:
            arr[position] = arr[position - gap]
            position = position - gap
            yield arr[::-1]

        arr[position] = current_value
        yield arr[::-1]
