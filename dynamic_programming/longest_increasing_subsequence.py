def longest_increasing_subsequence(arr):
    result = [1] * len(arr)
    for index in range(1, len(arr)) :
        for j in range(0, index):
            if arr[index] > arr[j]:
                if result[index] < result[j] + 1 :
                    result[index] = result[j] + 1
    print(result)

    # Printing LIS :
    min = max(result)
    min_ind = result.index(min)
    print(arr[min_ind])
    for index in range(len(result)-1, -1, -1):
        if min == result[index]+1 :
            print(arr[index])
            min = result[index]

    return max(result)


if __name__=="__main__":
    arr = [2,4,1,6,34,13,43,33]
    print(arr)
    result = longest_increasing_subsequence(arr)
    print("Longest increasing subsequence size is : ")
    print(result)
