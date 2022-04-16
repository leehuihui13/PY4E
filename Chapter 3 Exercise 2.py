H=input('Enter Hours: ')
R=input('Enter Rate: ')

try:
    if float(H)<=40:
        P=float(H)*float(R)
    elif float(H)>40:
        P=40*float(R)+(float(H)-40)*float(R)*1.5
    print('Pay:', P)

except:
    print('Error, please enter numeric input')
