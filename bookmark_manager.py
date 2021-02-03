# BOOKMARK MANAGER

lst = []
maxwebs = 5
while maxwebs > 0:
    newweb = input('Please enter the web name without the \'https://\' : ')
    lst.append(newweb.strip().lower())
    print(f't\The new web has been added with title \'https://{newweb}\'')
    maxwebs -= 1
    print(f'The are {maxwebs} place lefted')
    print(lst)
else:
    print('Sorry the bookmark is full you can\'t add more')
if len(lst) > 0:
    lst.sort()
    print('Here is the list of websites in your bookmark:')
    index = 0
    while index < len(lst):
        print(lst[index])
        index += 1
