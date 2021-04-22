""" Check Permutation """ 

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 , str2 = sorted(str1), sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True
print(check_permutation("abcd","bcad"))

def check_permutation2(str1,str2):
    if len(str1) != len(str2):
        return False
    str1, str2 = sorted(str1), sorted(str2)
    if str1 == str2:
        return True
    else:
        return False
print(check_permutation2("abcd","bcae"))