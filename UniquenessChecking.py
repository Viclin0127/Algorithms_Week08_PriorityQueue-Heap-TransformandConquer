# compare BruteForce method and Presorting method

from MergeSort import MergeSort
def BruteForce(A):
    n = len(A)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if A[i] == A[j]:
                return False
    return True

def PreSorting(A):
    n = len(A)
    MergeSort(A)
    for i in range (0, n-1):
        if A[i] == A[i+1]:
            return False
    return True

def test():
    A=[3, 1, 4, 5, 9, 2, 6, 8]
    print(BruteForce(A))
    print(PreSorting(A))
if __name__=="__main__":
    test()