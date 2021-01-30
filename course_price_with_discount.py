uname = input('please enter your name: ')
ucountry = input('please enter your country name: ')
isstudent = input('are you student? ')
cname = 'python course'
cprice = 100
if ucountry == 'Egypt':
    print(f'Hello {uname} because you are from {ucountry}')
    if isstudent == 'yes':
        print(f'and you are student the course price is {cprice - 80}$')
    else:
        print(f'the course price is {cprice - 70}$')
elif ucountry == 'ksa':
    print(f'Hello {uname} because you are from {ucountry}')
    if isstudent == 'yes':
        print(f'and you are student the course price is {cprice - 40}$')
    else:
        print(f'the course price is {cprice - 30}$')
elif ucountry == 'kanada':
    print(f'Hello {uname} because you are from {ucountry}')
    if isstudent == 'yes':
        print(f'and you are student the course price is {cprice - 20}$')
    else:
        print(f'the course price is {cprice - 10}$')
elif ucountry == 'usa':
    print(f'Hello {uname} because you are from {ucountry}')
    if isstudent == 'yes':
        print(f'and you are student the course price is {cprice - 10}$')
    else:
        print(f'the course price is {cprice}$')
else:
    print(f'Hello {uname} because you are from {ucountry}')
    if isstudent == 'yes':
        print(f'and you are the course price is {cprice - 25}$')
    else:
        print(f'the course price is {cprice - 20}$')
