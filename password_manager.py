# password manager
tries = 2
password = 'ahmed@'
inpassword = input('Please enter the password: ')
inpassword.lower().strip()
if inpassword == password:
    print('log in succeeded')
else:
    while tries > 0:
        inpassword = input(f'Please try again,{tries} chances left: ')
        tries -= 1
        if inpassword == password:
            print('log in succeeded')
            break

    else:
        print('Try again after 20 seconds')
