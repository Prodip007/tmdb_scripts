import os

dir_path = input('Enter the full path of the directory: ')

path_list = dir_path.split('/')
dir_name = path_list.pop()

total_subdir_list = []
for (path, dirs, files) in os.walk(dir_path):
    if dirs:
        total_subdir_list.append(dirs)

total_subdir_list.pop(0)

subdir_list_without_first_child = []
for subdirs in total_subdir_list:
    for subdir in subdirs:
        if subdir.__contains__('('):
            for index, char in enumerate(subdir):
                if char == "(":
                    name_without_braces = (subdir[:index-1])
                    subdir_list_without_first_child.append(name_without_braces)
        else:
            subdir_list_without_first_child.append(subdir)


with open('./sub_directory_names.txt', 'w') as output_file:
    for item in subdir_list_without_first_child:
        output_file.write("%s\n" %item)

# print(subdir_list_without_first_child)