def previous_smaller_element(A):
    if A :
        stack = []
        result = []
        result.append(-1)
        stack.append(0)
        for index in range(1,len(A)):
            if A[index] > A[stack[-1]]:
                result.append(stack[-1])
                stack.append(index)
            else:
                while stack and A[stack[-1]] >= A[index]:
                    stack.pop()
                if stack :
                    result.append(stack[-1])
                    stack.append(index)
                else:
                    result.append(-1)
                    stack.append(index)
        return result

def next_smaller_element(A):
    if A:
        stack = []
        result = [0] * len(A)
        result[-1] = len(A)
        stack.append(len(A)-1)
        for index in range(len(A)-2,-1,-1):
            if A[stack[-1]] < A[index]:
                result[index] = stack[-1]
                stack.append(index)
            else:
                while stack and A[stack[-1]] >= A[index]:
                    stack.pop()
                if stack :
                    result[index] = stack[-1]
                    stack.append(index)
                else:
                    result[index] = len(A)
                    stack.append(index)
        return result


if __name__ == "__main__":
    A = [4,2,1,5,6,3,2,4,2]
    psa = previous_smaller_element(A)
    nsa = next_smaller_element(A)

    max_area = -1
    for index in range(len(A)):
        curr_area = ( nsa[index] - psa[index] - 1 ) * A[index]
        if max_area < curr_area:
            max_area = curr_area
    print(max_area)
