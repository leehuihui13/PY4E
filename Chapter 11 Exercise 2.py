inp=input('Enter a file name:')
try:
    fhandle=open(inp)
except:
    print('Invalid file name',inp)
    quit()

import re
x2=[]
for line in fhandle:
    line=line.rstrip()
    x=re.findall('^New Revision: ([0-9]*)',line)
    if len(x)>0:
        for num in x:
            x2.append(int(num))
print(int(sum(x2)/len(x2)))
