'''
Question :
- Rotate matrix by 90, 180, 270

'''

def rotate_by_90_degree(arr):
    rows = len(arr)
    columns = len(arr[0])

    # Find the transpose
    for r in range(rows):
        for c in range(r+1, columns):
            arr[r][c], arr[c][r] = arr[c][r], arr[r][c]

    # Reverse Each Row
    for r in arr:
        for c in range(len(r)//2):
            r[c],r[len(r)-c-1] = r[len(r)-c-1],r[c]
    return arr


def rotate_by_180_degree(arr):
    arr_90 = rotate_by_90_degree(arr)
    arr_180 = rotate_by_90_degree(arr_90)
    return arr_180


def rotate_by_270_degree(arr):
    arr_90 = rotate_by_90_degree(arr)
    arr_180 = rotate_by_90_degree(arr_90)
    arr_270 = rotate_by_90_degree(arr_180)
    return arr_270


def rotate_by_360_degree(arr):
    arr_90 = rotate_by_90_degree(arr)
    arr_180 = rotate_by_90_degree(arr_90)
    arr_270 = rotate_by_90_degree(arr_180)
    arr_360 = rotate_by_90_degree(arr_270)
    return arr_360


if __name__=="__main__":
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    #arr = [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
    for index in range(len(arr)):
        print(arr[index])

    degree = 180
    if degree == 90:
        print("------- Rotate by 90 degrees -------")
        arr_90 = rotate_by_90_degree(arr)
        for index in range(len(arr_90)):
            print(arr_90[index])

    elif degree == 180:
        print("------- Rotate by 180 degrees -------")
        arr_180 = rotate_by_180_degree(arr)
        for index in range(len(arr_180)):
            print(arr_180[index])

    elif degree == 270:
        print("------- Rotate by 270 degrees -------")
        arr_270 = rotate_by_270_degree(arr)
        for index in range(len(arr_270)):
            print(arr_270[index])

    elif degree == 360:
        print("------- Rotate by 360 degrees -------")
        arr_360 = rotate_by_360_degree(arr)
        for index in range(len(arr_360)):
            print(arr_360[index])
