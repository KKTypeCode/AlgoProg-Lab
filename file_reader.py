with open('pi.txt', 'r') as file:
    x = file.readlines()[0]
    dictnum = {
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
        '0':0
    }
    for digit in x:
        for key,value in dictnum.items():
            if digit == key:
                dictnum[key] += 1
    
    print(dictnum)
    
with open('AlgoProg-Lab/test_text.txt', 'r') as file:
    x = file.readlines()
    print(x)
    num = x[0]
    z = float(num) + 1
    add = x[1]

with open('AlgoProg-Lab/test_text.txt', 'w') as file:
    file.write(str(z))
    file.write(add)