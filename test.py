def removeDuplicates(S: str) -> str:
    i, le = 1, len(S)
    preIndex = 0
    while i < le:
        val = S[i]
        if val != S[preIndex]:
            preIndex = i
            i += 1
        else:
            S = S[0:preIndex]+(S[i+1:] if i+1 < le else "")
            print('>>', preIndex, i+1)
            print("S:", S)
            le = len(S)
            i = 1
            preIndex = 0
    return S


print(removeDuplicates("aababaab"))
