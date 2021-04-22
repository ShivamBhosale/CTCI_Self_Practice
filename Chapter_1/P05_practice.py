"""Check if a string can converted to another string with a single edit"""

#one_edit_different
def one_edit_different(str1,str2):
    if len(str1) == len(str2):
        return one_edit_replace(str1,str2)
    if len(str1) +1 == len(str2):
        return one_edit_replace(str1,str2)
    if len(str1) -1 == len(str2):
        return one_edit_replace(str1,str2)
    return False

def one_edit_replace(str1,str2):
    edited = False
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True

print(one_edit_different("pale","gale"))