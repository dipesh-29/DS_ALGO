def searching_in_array(arr, num, low, high):
    mid = (low + high)/2
    if arr[mid] == num:
        return mid
    if num >= arr[mid] and num <= arr[high]:
        searching_in_array(arr, num, mid)
