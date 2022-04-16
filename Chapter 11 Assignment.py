inp=input('Enter file name:')
try:
    fhandle=open(inp)
except:
    print('Invalid file name')
    exit()

import re
x2=[]
for line in fhandle:
    line=line.rstrip()
    x=re.findall('([0-9]+)',line)
    if len(x)>0:
        for num in x:
            x2.append(int(num))
print(sum(x2))
