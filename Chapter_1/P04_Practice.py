""" Palindrome Permutation - function checks if a string is a permutation of a palindrome or not """

def pal_perm(str1):
    str1 = str1.replace(" ","").lower()

    d = dict()

    for i in str1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k,v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False

    return True


print(pal_perm("racecar"))
        