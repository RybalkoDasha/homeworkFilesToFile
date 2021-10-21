import os.path


def search_file_in_catalog(catalog_name, result_file):
    files_dict = {}

    for file in os.listdir(catalog_name):
        if file.endswith(".txt") and file != result_file:
            with open(catalog_name + '/' + file, encoding='utf8') as f:
                lens = f.readlines()
            files_dict[file] = len(lens)

    print(files_dict)
    sorted_list = sorted(files_dict.values())
    print(sorted_list)

    with open(catalog_name + '/' + result_file, "w", encoding='utf8') as file_write:
        for el in sorted_list:
            for key, val in files_dict.items():
                if el == val:
                    print(key)
                    file_write.write(key + '\n')
                    file_write.write(str(val) + "\n")
                    with open(catalog_name + '/' + key, encoding='utf8') as file_read:
                        for line in file_read.readlines():
                            file_write.write(line.strip() + '\n')





catalog_name = input('Введите каталог: ')
# catalog_name = 'c:/testpy'
result_file = 'result.txt'
search_file_in_catalog(catalog_name, result_file)
