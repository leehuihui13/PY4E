def count(word):
    num=0
    for letter in word:
        if letter == 'a':
            num=num+1
    return num

inpword=input('Enter a word:')
numofa=count(inpword)
print(numofa)
