peoples = {
    'osama': {
        'html': '90%',
        'css': '80%',
        'js': '75%'
    },
    'ahmed': {
        'html': '98%',
        'css': '88%',
        'js': '70%'

    },
    'sayed': {
        'html': '95%',
        'css': '85%',
        'js': '55%'
    }
}


def show_skills(**peoples):
    for name in peoples:
        print(f'skills of {name} are: ')
        for skills, progress in peoples[name].items():
            print(f'{skills} ==> {progress}')


show_skills(**peoples)
