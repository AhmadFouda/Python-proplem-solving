admins = ['Ahmed', 'Osama', 'Sameh', 'Manal', 'Rahma', 'Mahmoud', 'Enas']
name = input('please enter your name: ').strip().capitalize()
if name in admins:
    print(f'Hello {name} welcome back')

    option = input('delete or ubdate your name? ').strip().capitalize()
    if option == 'Update' or option == 'U':
        newname = input('enter your new name: ').strip().capitalize()
        admins[admins.index(name)] = newname
        print('name updated.')
        print(admins)
    elif option == 'Delete' or option == 'D':
        # admins.remove(name)
        del admins[admins.index(name)]
        print('name deleted.')
        print(admins)
    else:
        print('wrong option')
else:
    adding_option = input(
        f'you are not an admin {name}, do you want to be an admin? ').strip().capitalize()
    if adding_option == 'Yes':
        admins.append(name)
        print('name added, now you are an admin with us')
        print(admins)
    elif adding_option == 'No':
        print('ok thanks')
    else:
        print('Error')
