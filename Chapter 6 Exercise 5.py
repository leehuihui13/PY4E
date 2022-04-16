data= 'X-DSPAM-Confidence:0.8475'
pos1=data.find(':')
num=data[pos1+1:]
print(float(num))
