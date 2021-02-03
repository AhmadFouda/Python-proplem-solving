############################################ age calculator in different uints ###########################################
numprocess = int(
    input('please chose the number of process: 1.months, 2.weeks, 3.days: '))
age = input('plese enter your age: ')
months = int(age) * 12
weeks = months * 4
days = int(age) * 365
if numprocess == 1:
    print('you chosed the unit month,')
    print(f'you lived for {months} month')
elif numprocess == 2:
    print('you chosed the unit weeks,')
    print(f'you lived for {weeks} week')
elif numprocess == 3:
    print('you chosed the unit days,')
    print(f'you lived for {days} day')
