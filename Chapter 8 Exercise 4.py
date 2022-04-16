fname=input("Enter file name: ")

try:
    fhand=open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

x=[]
for line in fhand:
    apline=line.split()
    for word in apline:
        if word not in x:
            x.append(word)
    x.sort()
print(x)
