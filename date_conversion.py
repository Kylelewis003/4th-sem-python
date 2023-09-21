def convertdate(s):
    str1 = s.split("-")
    if len(str1) == 3:
        if len(str1[0]) == 4:
            year , month , day = str1
            str2 = f"{day}-{month}-{year}"
            return str2
        elif len(str1[0]) == 2:
            return s
s = input("Enter a date : ")
print("Converted date is : ",convertdate(s))