def Possibility (N, M, A):
    flag = 0
    if(N == 1):
        return flag
    
    
    elif(N == 2):
        i = 0
        B = A.copy()
        B.sort()
        if(A == B and A[i] != A[i + 1]):
            return flag+1
        else:
            return flag
    else:
        i = 0
        count = 0
        s= []
        C = A.copy()
        for i in range(len(A) - 2):
            s.append(C[i] +  C[i + 1] +  C[i + 2])
            k = A[:i] + s + A[i+3:]
            s.pop()
            L = k.copy()
            L.sort()
            if(L == k):
                count = 1
            else:
                count = 0
        return count
    
Possibility(4, 2, [1, 2, 1, 2])
