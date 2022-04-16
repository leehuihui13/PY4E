Score=input('Enter score: ')

try:
#taking sco from the local scope (within the function)
    def computegrade(sco):
        if float(sco)>=0.9 and float(sco)<=1.0:
            return'A'
        elif float(sco)>=0.8 and float(sco)<0.9:
            return'B'
        elif float(sco)>=0.7 and float(sco)<0.8:
            return'C'
        elif float(sco)>=0.6 and float(sco)<0.7:
            return'D'
        elif float(sco)<0.6 and float(sco)>=0.0:
            return'F'

#taking value Score from the global scope (input)
    Result=computegrade(Score)
    print(Result)

except:
    print('Bad score')
