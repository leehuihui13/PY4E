Hours=input('Enter Hours: ')
Rate=input('Enter Rate: ')

try:
#taking H,R from the local scope (within the function)
    def computepay(H,R):
        if float(H)<=40:
            P=float(H)*float(R)
            return P
        if float(H)>40:
            P=40*float(R)+(float(H)-40)*float(R)*1.5
            return P

#taking value Pay from the global scope (input)
    Pay=computepay(Hours,Rate)
    print('Pay: ',Pay)

except:
    print('Error, please enter numeric input')
