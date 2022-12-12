import os

dir_path = input('Enter the full path of the directory: ')

path_list = dir_path.split('/')
dir_name = path_list.pop()


list_of_subdir = os.listdir(dir_path)

new_list_of_subdir = []

for item in list_of_subdir:
    if os.path.isdir(dir_path+"/"+item):
        if(item[0] != '.'):
            new_list_of_subdir.append(item)


with open('./sub_directory_names.txt', 'w') as output_file:
    for item in new_list_of_subdir:
        output_file.write("%s\n" %item)

    print('All the name of the sub directories in "%s" are now printed on sub_directory_names.txt file' %dir_name)