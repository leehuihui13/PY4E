fname=input('Enter a file name: ')
try:
    fhandle=open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts=dict()
for line in fhandle:
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        word=words[2]
        counts[word]=counts.get(word,0)+1
print(counts)
