def display_n_lines(a , n):
    with open(a , 'r' )  as file:
        for i in range(n):
            line = file.readline()
            if line:
                print(line)
            else:
                print("End of file")
                break

def occurances_word(a , word):
    with open(a , 'r') as file:
        content = file.read()
        word_count = content.lower().count(word.lower())
        print(word , "occurs" , word_count , "times in the file")


a = input("Enter the file name :")

n  =int(input("\nEnter the number of lines to display :"))
print("\nFirst",n,"line of the file are : \n")
display_n_lines(a,n)

word = input("\nEnter the word to find occurances for : ")
occurances_word(a,word)


    