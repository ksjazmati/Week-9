def letterIdentfier(string):
    vow=0
    con=0
    for char in string:
        if (char== 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char== 'I' or char == 'O' or char == 'U'):
            vow+=1
        else:
            con+=1
    print("Number of vowels: ", vow)
    print("Number of consonants: ", con)


def main():
    newString = ''
    newString = input("Input a string: ")
    letterIdentfier(newString)
main()