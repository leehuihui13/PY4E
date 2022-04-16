fname=input('Enter a file name: ')
try:
    fhandle=open(fname)
except:
    print('Invalid file name', fname)
    quit()

d=dict()

for line in fhandle:
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        word=words[5]
        time=word.split(':')
        d[time[0]]=d.get(time[0],0)+1

l=list()
for k,v in d.items():
    l.append((k,v))
    l.sort()
for k,v in l:
    print(k,v)


#x= sorted([(int(k),v)for k,v in d.items()])
#print(*x, sep="\n")
