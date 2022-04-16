fhand=open('mbox-short.txt')
count=0
for line in fhand:
    words=line.split()
    #print('Debug:', words)
    #guardian in compound statement, guardian needs to come before!
    #If the first part is true, it causes a "short circuit evaluation"
    if len(words)<3 or words[0]!='From':
        continue
    print(words[2])
