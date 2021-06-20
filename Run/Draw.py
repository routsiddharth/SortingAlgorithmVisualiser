import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def hex_to_rgb(value):

    value = value.lstrip('#')
    lv = len(value)

    res = []

    for i in range(0, lv, lv // 3):
        res.append(int(value[i:i + lv // 3], 16))

    res.append(256)

    for i in range(len(res)):
        res[i] = round(res[i] / 256, 3)

    return res

def Draw(id, length, colour, frames, gradient=False, reverse=False, trueRandom=False):

    if reverse:
        from Algorithms.Descending import BubbleSort, QuickSort, InsertionSort, SelectionSort, CocktailSort
        from Algorithms.Descending import CountSort, MergeSort, HeapSort, ShellSort, GnomeSort

    else:
        from Algorithms.Ascending import BubbleSort, QuickSort, InsertionSort, MergeSort, CocktailSort
        from Algorithms.Ascending import CountSort, SelectionSort, HeapSort, ShellSort, GnomeSort

    if trueRandom:
        arr = [random.randint(1, 100) for i in range(length)]
    else:
        arr = [i + 1 for i in range(length)]

    random.shuffle(arr)

    if gradient == 1:
        colour = [hex_to_rgb(colour) for _ in range(length)]

        difference = round(1 / length, 5)

        for i in range(len(colour)):
            alpha = i * difference

            if alpha < 0.1:
                alpha = 0.1

            colour[i][3] = alpha

    if id == "BubbleSort":
        title = f"Bubble Sort - {len(arr)} Elements"
        array = BubbleSort.BubbleSort(arr)
    elif id == "QuickSort":
        title = f"Quick Sort - {len(arr)} Elements"
        array = QuickSort.QuickSort(arr, 0, len(arr) - 1)
    elif id == "InsertionSort":
        title = f"Insertion Sort - {len(arr)} Elements"
        array = InsertionSort.InsertionSort(arr)
    elif id == "MergeSort":
        title = f"Merge Sort - {len(arr)} Elements"
        array = MergeSort.MergeSort(arr, 0, len(arr) - 1)
    elif id == "CountSort":
        title = f"Count Sort - {len(arr)} Elements"
        array = CountSort.CountSort(arr)
    elif id == "ShellSort":
        title = f"Shell Sort - {len(arr)} Elements"
        array = ShellSort.ShellSort(arr)
    elif id == "HeapSort":
        title = f"Heap Sort - {len(arr)} Elements"
        array = HeapSort.HeapSort(arr)
    elif id == "SelectionSort":
        title = f"Selection Sort - {len(arr)} Elements"
        array = SelectionSort.SelectionSort(arr)
    elif id == "GnomeSort":
        title = f"Gnome Sort - {len(arr)} Elements"
        array = GnomeSort.GnomeSort(arr)
    elif id == "CocktailSort":
        title = f"Cocktail Sort - {len(arr)} Elements"
        array = CocktailSort.CocktailSort(arr)

    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rec = ax.bar(range(len(arr)), arr, align='edge', color=colour)

    ax.set_xlim(0, length)
    ax.set_ylim(0, int(max(arr) * 1.1))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_plot(arr, rec, operations):

        for rec, val in zip(rec, arr):
            rec.set_height(val)

        operations[0] += 1

        text.set_text(f"Operations: {operations[0]}")

    animation = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, [0]), frames=array, interval=frames, repeat=False)

    plt.show()