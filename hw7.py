# Напишите программу, которая читает данные из файлов
# /etc/passwd и /etc/group на вашей системе и выводит
# следующую информацию в файл output.txt:
# 1. Количество пользователей, использующих все имеющиеся
# интерпретаторы-оболочки.
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)

from collections import Counter


out = open('output.txt', 'w')
f = open('passwd.txt')
print('---SHELLS---\n', file=out)
users = f.readlines()
users = [i.rstrip('\n') for i in users]
user_list = [i.split(':') for i in users]
shells = [i[6] for i in user_list]
shells_count = dict(Counter(shells))
print(shells_count)
for key, value in shells_count.items():                      
    print(key, ' - ', value, file=out)

print('\n---GROUPS---\n', file=out)

fg = open('group.txt')
groups = fg.readlines()
groups = [i.rstrip('\n') for i in groups]
group_list = [i.split(':x:') for i in groups]
for key, value in dict(group_list).items():
    print(key, ':', value, file=out)

f.close()
fg.close()
out.close()