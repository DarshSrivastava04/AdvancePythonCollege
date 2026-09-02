def Find_LCS(A,B):
    m = len(A)
    n = len(B)
    lcs = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            elif A[i-1] != B[j-1]:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])

    i = m
    j = n
    lcstr = ''
    while i>0 and j>0:
        if A[i-1] == B[j-1]:
            lcstr += A[i-1]
            i -= 1
            j -= 1
        elif lcs[i-1][j]>lcs[i][j-1]:
            i-=1
        else:
            j-=1
    return lcstr[::-1]

print(Find_LCS(input("A:"),input("B:")))