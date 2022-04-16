name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

tmp=list()
for k,v in counts.items():
    newt=(v,k)
    tmp.append(newt)

tmp=sorted(tmp,reverse=True)
for v,k in tmp[:5]:
    print(k,v)
    
#bigcount = None
#bigword = None
#for word, count in list(counts.items()):
#    if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count

#print(bigword, bigcount)
