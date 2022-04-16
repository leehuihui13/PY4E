fname=input('Enter a file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

wordkey=dict()
count=0
for line in fhand:
    words=line.split()
    for word in words:
        wordkey[word]=count
        count=count+1
        
wordcheck=input('Enter a word: ')
print (wordcheck in wordkey)
