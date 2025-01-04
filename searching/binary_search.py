def binary_search(A,low,high,target):
    if low > high :
        return -1
    else:
        mid = int((low + high) / 2)
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            x = binary_search(A,mid+1,high,target)
        else:
            x = binary_search(A,low,mid-1,target)
        return x


if __name__=="__main__":
    A = [1,2,4,5,6,6,8,9,10,14,16,18]
    target = 20
    result = binary_search(A,0,len(A),target)
    print(result)
