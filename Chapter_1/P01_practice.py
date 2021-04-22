""" Is Unique """
def isUnique(str1):
    sorted_str = sorted(str1)
    last_character = None
    for charz in sorted_str:
        if charz == last_character:
            return False
        last_character = charz
    return True

print(isUnique("Helo"))

""" is Unique in a pythonic way """

def isUnique_pythonic(str2):
    return len(set(str2)) == len(str2)

print(isUnique_pythonic("Hello"))
