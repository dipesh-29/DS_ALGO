def string_permutation(A,index):
    if index == len(A)-1:
        print(A)
        return

    for i in range(index, len(A)):
        A[i],A[index] = A[index],A[i]
        string_permutation(A,index+1)
        A[i],A[index] = A[index],A[i]



if __name__ == '__main__':
    A = ['A','B','C','D']
    string_permutation(A,0)
