def count_vowel(word):
    vowel = "aeiouAEIOU"
    count = 0
    for i in word:
        if i in vowel:
            count+=1
    return count

def find_word(s):
    words = s.split(" ")
    max_vowel = 0
    word_max_vowel = ""
    for i in words:
        vowels = count_vowel(i)
        if vowels > max_vowel:
            max_vowel = vowels
            word_max_vowel = i
    return word_max_vowel

s = input("Enter a scentence : ")
print("The word with the most vowels is : ",find_word(s))