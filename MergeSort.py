# MergeSort Method
# stable
# Not in-place
# O(nlogn)

def MergeSort(A):
    if len(A) > 1:
        n = len(A)
        B = A[:n//2]
        C = A[n//2:]
        MergeSort(B)
        MergeSort(C)
        Merge(B,C,A)

def Merge(B,C,A):
    i = j = k = 0
    p = len(B)
    q = len(C)
    while i < p and j < q:
        if B[i] <= C[j]:     # this is the important part that MergeSort could be stable if we use <=
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    if i == p:
        A[k : p+q] = C[j : q]
    else:
        A[k : p+q] = B[i : p]

def test():
    A = [8,7,5,4,3,2,1]
    MergeSort(A)
    print(A)

if __name__ == "__main__":
    test()