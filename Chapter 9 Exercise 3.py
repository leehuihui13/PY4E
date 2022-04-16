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
        word=words[1]
        counts[word]=counts.get(word,0)+1
print(counts)
