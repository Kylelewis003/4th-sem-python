import difflib

def stringsimilar(str1 , str2):
    result = difflib.SequenceMatcher(a = str1.lower() , b = str2.lower())
    return result.ratio()

str1  = "Python Program"
str2 = "Python Progra"

print(stringsimilar(str1 , str2))