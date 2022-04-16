fname=input('Enmbter a file name: ')
try:
    fhandle=open(fname)
except:
    print('File cannot be opened', fname)
    quit()

di=dict()
for line in fhandle:
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        di[words[1]]=di.get(words[1],0)+1
#print(di)

li=list()
for k,v in di.items():
    li.append((v,k))
li.sort(reverse=True)
#print(li)
#print(li[0])

#cannot print li[0] because py identifies it as a tuple, cannot iterate 2 values at the same time
for v,k in li[:1]:
    print(k,v)
