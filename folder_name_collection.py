import os

dir_path = input('Enter the full path of the directory: ')

path_list = dir_path.split('/')
dir_name = path_list.pop()


list_of_subdir = os.listdir(dir_path)

# subdirs = [x[1] for x in os.walk(dir_path)]

# new_list_of_subdir = []

# for item in list_of_subdir:
#     if os.path.isdir(dir_path+"/"+item):
#         if(item[0] != '.'):
#             new_list_of_subdir.append(item)


# with open('./sub_directory_names.txt', 'w') as output_file:
#     for item in new_list_of_subdir:
#         output_file.write("%s\n" %item)

#     print(new_list_of_subdir)

#     print('All the name of the sub directories in "%s" are now printed on sub_directory_names.txt file' %dir_name)

# subdirs = os.walk(dir_name)

# for item in subdirs:
#     print(item)

# print(subdirs[1])

# print(subdirs)

total_list = []

for (path, dirs, files) in os.walk(dir_path):
    # print(path)
    if dirs:
        total_list.append(dirs)
        # print(dirs)
        # print("--------")
    # print(files)


total_list.pop(0)

# print(total_list)

new_total_list = []

for item in total_list:
    for i in item:
        new_total_list.append(i)


for index, char in enumerate(new_total_list[1]):
    if char == "(":
        new_name = (new_total_list[1])[:index]
        print(new_name)

# print(new_total_list)

# with open('./sub_directory_names.txt', 'w') as output_file:
#     for item in new_total_list:
#         output_file.write("%s\n" %item)
