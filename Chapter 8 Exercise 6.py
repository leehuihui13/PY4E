nums=[]
while True:
    inp=input('Enter a number: ')
    if inp=='done':
        break
    try:
        nums.append(int(inp))
    except:
        print('Invalid input')

print(nums)
print(max(nums))
print(min(nums))
