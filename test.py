def gcdOfStrings(str1: str, str2: str) -> str:
    for i in range(len(str1), -1, -1):
        print("I : ",i)
        print(">>> ", str1.replace(str1[:i], ""), str2.replace(str1[:i], ""))
        if str1.replace(str1[:i], "") == "" and str2.replace(str1[:i], "") == "":
            return str1[:i]
    return ""


str1, str2 = "ABABAB", "ABAB"
# print("MMM: ", str2.replace(str2[: 50], ""))
print(gcdOfStrings(str1, str2))
