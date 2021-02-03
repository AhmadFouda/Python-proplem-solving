admins = ['ahmed', 'fouda', 'emad', 'nasser']
name = input('please type your name: ')
if name in admins:
    print(f'Hello {name} you are an admin with us.')
    option = input('delete(d) or update(u) your name? ')
    if option == 'update' or option == 'u':
        newname = input('please enter your new name: ')
        admins[admins.index(name)] = newname
        print(f'your new name is {newname}.')
        print('name updated.')
        print(admins)
    elif option == 'delete' or option == 'd':
        admins.remove(name)
        print('your name has been deleted.')
        print(admins)
    else:
        print('wrong option')
else:
    status = input(
        f'sorry {name} you are not an admin with us, do you want to be an admin? yes or no: ')
    if status == 'yes' or status == 'y':
        admins.append(name)
        print('you have been added')
        print(admins)
    if status == 'no' or status == 'n':
        print('ok as you like.')
