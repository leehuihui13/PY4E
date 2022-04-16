total=0.0
count=0

while True:
    num=input('Enter a number: ')
    try:
        total=total+float(num)
        count=count+1
        continue
    except:
        print('Invalid input')
    if num=='done':
        break

print(total, count, total/count)

