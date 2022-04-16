fname=input('Enter a file name: ')
count=0
total=0

try:
    fhandle=open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence: '):
        count=count+1
        num=line[20:]
        total=total+float(num)

print('Average spam confidence:', total/count)
        
