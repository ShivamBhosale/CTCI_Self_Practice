""" Urlify """
def urlify(str1, length):
    str1 = str1[:length]
    str1=str1.replace(" ","%20")
    return str1

print(urlify("Shivam Bhosale   ",14))