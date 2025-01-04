'''
Question :
Find tehe transpose of nxn matrix.
'''

def transpose(arr):
    rows = len(arr)
    columns = len(arr[0])
    for r in range(rows):
        for c in range(r+1, columns):
            arr[r][c], arr[c][r] = arr[c][r], arr[r][c]
    return arr



if __name__=="__main__":
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    for index in range(len(arr)):
        print(arr[index])
    arr = transpose(arr)
    print("------- Transpose -------")
    for index in range(len(arr)):
        print(arr[index])
