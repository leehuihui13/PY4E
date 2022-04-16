fname=input('Enter a file name: ')
count=0

if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fhandle=open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
for line in fhandle:
    count=count+1

print('There were',count,'subject lines in',fname)
        
