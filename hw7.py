# Напишите программу, которая читает данные из файлов
# /etc/passwd и /etc/group на вашей системе и выводит
# следующую информацию в файл output.txt:
# 1. Количество пользователей, использующих все имеющиеся
# интерпретаторы-оболочки.
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)


passwd_file = open('passwd.txt')
users_dict = {}
shell_count = {}
for line in passwd_file:
    user_id = line.rstrip().split(':')[2]
    group_id = line.rstrip().split(':')[3]
    shell = line.rstrip().split(':')[-1]
    if shell not in shell_count:
        shell_count[shell] = 1
    else:
        shell_count[shell] += 1
    users_dict[user_id] = int(group_id)

groups_file = open('group.txt')
group_dict = {}
for line in groups_file:
    group_name = line.rstrip().split(':')[0]
    group_id = line.rstrip().split(':')[2]
    group_dict[int(group_id)] = group_name
groups_file.close()

def print_dict(my_dict):
    res = ''
    for item, amount in my_dict.items():
        res = res + f'{amount} - {item}' + ' ; '
    return res

def users_search(group_dict, users_dict):
    res = ''
    for group_id, group_name in group_dict.items():
        users_id = [user_id for (user_id, user_group_id) in users_dict.items() if group_id == user_group_id]
        if len(users_id) != 0:
            res = res + "{}: {}".format(group_name, ",".join(users_id)) + " , "
    return res

with open('output_file.txt', 'a') as out_file:
    out_file.write(print_dict(shell_count))
    out_file.write('\n')
    out_file.write(users_search(group_dict, users_dict))

passwd_file.close()
groups_file.close()
out_file.close()