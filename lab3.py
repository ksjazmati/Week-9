def _encrypt(string1):
    string2 = ''
    for i in string1:
        string2 += chr(ord(i)+4)
    return string2

def _decrypt(string1):
    string2 = ' '
    for i in string1:
        string2 += chr(ord(i)-4)
    return string2
    
def main():
    newString = input("Enter a string to encrypt: ")
    newString = _encrypt(newString.replace(" ", ""))
    print("Unsecured:", _decrypt(newString))
    print("Secured:  ", newString)
    
main()
