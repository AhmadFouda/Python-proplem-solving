################### PRACTICAL_ EMAIL SLICING ##########################

name = input('please enter your name: ')
email = input('please enter your email: ')
name = name.strip().capitalize()

username = email[:email.index('@')]
username = username.strip().capitalize()
website = email[email.index('@') + 1:]
print(f'Hello {name} we are happy to meet you, ')
print(f'your username is {username} and your website is {website}')
