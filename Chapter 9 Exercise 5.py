fname=input('Enter file name: ')
try:
    fhandle=open(fname)
except:
        print('File cannot be opened', fname)
        quit()
        
counts=dict()
for line in fhandle:
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
#double split, variable email becomes a str where you can apply split
        email=words[1]
        words1=email.split('@')
        word=words1[1]
        counts[word]=counts.get(word,0)+1
print(counts)
