def sumN(list):
    nList = []
    nList.append(list[0] + list[1])
    i = 1
    while i < len(list) - 1:
        nList.append(list[i - 1] + list[i] + list[i + 1])
        i += 1
    nList.append(list[i - 1] + list[i])

    return nList

def main():
    list = [10,20,30,40,50]
    print(sumN(list))
    
main()