print('*' * 50)

mytuple = ('python', 'html', 'css')
mydict = {'python': '95%', 'css': '60%', 'html': '80%'}


def show_skills(name, *skills, **skills_with_progress):
    print(f'Hello {name.capitalize()}')
    print(f'your skills without progress are: ')
    for skill in skills:
        print(f'- {skill}')
    print('your skills with progress are: ')
    for key_skill, value_progress in skills_with_progress.items():
        print(f'{key_skill} ==> {value_progress}')


show_skills('ahmed', *mytuple, **mydict)
