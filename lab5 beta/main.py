with open('num.txt', 'r') as file:
    num = list(file.read())
    num.reverse()
    sum = 0
    for i in range(len(num)):
        if num[i] == '1':
            sum += 2 ** (i % 4)
    if sum % 15 == 0:
        print('yes')
    else:
        print('no')
    print(sum)