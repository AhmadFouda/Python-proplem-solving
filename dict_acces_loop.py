
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
for name in peoples:
    print(f'skills and progress of {name} are:')
    for skill in peoples[name]:
        print(f'- {skill.upper()} ==> {peoples[name][skill]}')
print('*' * 10)
for main_key, main_value in peoples.items():
    print(f'skills and progress of {main_key} are:')
    for child_key, child_value in main_value.items():
        print(f'- {child_key} ==> {child_value}')
