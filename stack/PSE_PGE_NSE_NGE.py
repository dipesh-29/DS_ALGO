'''
Given an array of positive numbers, print the previous smaller element of each number. If there is no smaller element previously then print -1.


1. Previous Smaller Element
2. Next Smaller Element
3. Previous Greater Element
4. Next Greater Element

'''

def previous_smaller_element(A):
    if A :
        stack = []
        result = []
        result.append(-1)
        stack.append(A[0])
        for item in A[1:]:
            if item > stack[-1]:
                result.append(stack[-1])
                stack.append(item)
            else:
                while stack and stack[-1] >= item:
                    stack.pop()
                if stack :
                    result.append(stack[-1])
                    stack.append(item)
                else:
                    result.append(-1)
                    stack.append(item)
        return result


def previous_greater_element(A):
    if A :
        stack = []
        result = []
        result.append(-1)
        stack.append(A[0])
        for item in A[1:]:
            if item < stack[-1]:
                result.append(stack[-1])
                stack.append(item)
            else:
                while stack and stack[-1] <= item:
                    stack.pop()
                if stack:
                    result.append(stack[-1])
                    stack.append(item)
                else:
                    result.append(-1)
                    stack.append(item)
        return result


def next_smaller_element(A):
    if A:
        stack = []
        result = [0] * len(A)
        result[-1] = -1
        stack.append(A[-1])
        for index in range(len(A)-2,-1,-1):
            if stack[-1] < A[index]:
                result[index] = stack[-1]
                stack.append(A[index])
            else:
                while stack and stack[-1] >= A[index]:
                    stack.pop()
                if stack :
                    result[index] = stack[-1]
                    stack.append(A[index])
                else:
                    result[index] = -1
                    stack.append(A[index])
        return result


def next_greater_element(A):
    if A :
        stack = []
        result = [0] * len(A)
        result[-1] = -1
        stack.append(A[-1])
        for index in range(len(A)-2,-1,-1):
            if stack[-1] > A[index]:
                result[index] = stack[-1]

            else:
                while stack and stack[-1] <= A[index] :
                    stack.pop()
                if stack:
                    result[index] = stack[-1]
                else:
                    result[index] = -1
            stack.append(A[index])
        return result



if __name__ == '__main__':
    A = [4,10,5,8,20,15,3,12]
    #A = []
    result = previous_smaller_element(A)
    #result = previous_greater_element(A)
    #result = next_smaller_element(A)
    #result = next_greater_element(A)
    print(result)
