fname=input('Enter a file name: ')
try:
    fhandle=open(fname)
except:
    print('Invalid file name',fname)
    quit()

counts=dict()
import string
for line in fhandle:
    line=line.strip() #strip white space///string
    line=line.translate(line.maketrans('','',string.punctuation)) #remove punctuation///string
    line=''.join([i for i in line if not i.isdigit()]) #remove numbers///string
    line=line.lower() #lower capital///string
    line=line.replace(' ','') #remove spacing
    letters=list(line)  #convert string of words to list of letters
    for letter in letters:
        counts[letter]=counts.get(letter,0)+1

lst=list()
for k,v in counts.items():
    lst.append((v,k))
    lst.sort(reverse=True)
print(lst)
