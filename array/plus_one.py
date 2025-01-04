def plusOne(self, A):
        result = A
        c = 0
        carry = 0
        while(c != len(A)-1):
            if A[len(A)-c-1] == 9:
                result[len(A)-c-1] = 0
                c += 1
                carry = 1
            else:
                result[len(A)-c-1] = A[len(A)-c-1] + 1
                c += 1
                carry = 0
                break
        if carry:
            if len(A)-c-1 == 0 :
                if A[0] == 9:
                    result[0] = 0
                    result.insert(0,1)
                else:
                    result[0] = A[0] + 1
            else:
                result[len(A)-c-1] = A[len(A)-c-1] + 1
        else:
            if len(A) == 1:
                if A[0] == 9:
                    result[0] = 0
                    result.insert(0,1)
                else:
                    result[0] = A[0]+1

        while(result):
            if result[0] == 0:
                result.remove(0)
            else:
                break

        return result
