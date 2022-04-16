H=input('Enter Hours: ')
R=input('Enter Rate: ')

if float(H)<=40:
    P=float(H)*float(R)
if float(H)>40:
    P=40*float(R)+(float(H)-40)*float(R)*1.5
print('Pay:', P)
