# Напишите программу, которая читает данные из файлов
# /etc/passwd и /etc/group на вашей системе и выводит
# следующую информацию в файл output.txt:
# 1. Количество пользователей, использующих все имеющиеся
# интерпретаторы-оболочки.
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)

shells = {}
groups = {}
name_to_UID = {}

shell_index = 6
group_index = 4
uid_index = 2
name_index = 0

with open('passwd.txt', 'r') as file:
    for line in file:
        fields = line.rstrip().split(":")
        shells[fields[shell_index]] = shells.get(fields[shell_index], 0) + 1
        name_to_UID[fields[name_index]] = fields[uid_index]

group_index = 0

with open('group.txt', 'r') as file:
    for line in file:
        fields = line.rstrip().split(":")
        if fields[group_index] in name_to_UID:
            groups[fields[group_index]] = name_to_UID[fields[group_index]]
        if fields[3] != '':
            users = fields[3].split(",")
            for user in users:
                uid = name_to_UID[user]
                if fields[group_index] in groups:
                    groups[fields[group_index]] = groups[fields[0]] + "," + uid
                else:
                    groups[fields[group_index]] = uid

with open('output.txt', 'w') as file:
    for sh in shells:
        file.write("%s - %d ; " % (sh, shells[sh]))
    file.write("\n")
    for g in groups:
        file.write("%s:%s ; " % (g, groups[g]))

