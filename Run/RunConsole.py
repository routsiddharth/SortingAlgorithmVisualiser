from Run import Draw

def main():

    n = int(input("Enter the number of elements:\n"))
    al = int(input("Choose algorithm:  1.Bubble \n 2.Insertion \n 3.Quick \n 4.Selection \n 5.Merge Sort \n 6.Heapify \n 7.Shell \n 8.Count sort\n"))

    if(al==1):
        Draw.Draw("BubbleSort", n, "#33CCFF")
    elif(al==2):
        Draw.Draw("InsertionSort", n, "#33CCFF")
    elif(al==3):
        Draw.Draw("QuickSort", n, "#33CCFF")
    elif(al==4):
        Draw.Draw("SelectionSort", n, "#33CCFF")
    elif (al == 5):
        Draw.Draw("MergeSort", n, "#33CCFF")
    elif (al == 6):
        Draw.Draw("HeapSort", n, "#33CCFF")
    elif (al == 7):
        Draw.Draw("ShellSort", n, "#33CCFF")
    elif (al == 8):
        Draw.Draw("CountSort", n, "#33CCFF")