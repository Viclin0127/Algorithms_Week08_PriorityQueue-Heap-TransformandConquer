# How to find the mode in an array
# sorting first makes problem easier and more efficient
# sorting takes O(nlogn) and finding mode takes linear time

from MergeSort import MergeSort
def ModeFinding(A)
    n = len(A)
    MergeSort(A)
    i = 0
    maxFreq = 0
    while i < n :
        runlength = 1
        while (i + runlength < n) and (A[i] == A[i + runlength]):
            runlength += 1
        if runlength > maxFreq :
            maxFreq = runlength
            mode = A[i]
        i += 1
    return mode

def test():
    A = [42, 78, 13, 13, 57, 42, 57, 78, 13, 98, 42, 33]
    print(ModeFinding(A))

if __name__=="__main__":
    test()