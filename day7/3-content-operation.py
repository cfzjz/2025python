import os


def use_rename():
    # os.rename('test\\ftest', 'test\\fftt')
    os.remove('test\\fftt')


def use_dir_content():
    print(os.listdir('.'))
    # os.mkdir('dir2')
    # os.rmdir('dir2')
    print(os.path.isdir('test'))
    os.chdir('test')
    print(os.getcwd())
    f = open('tt', encoding='utf-8')
    print(f.read())
    f.close()


def scan_dir(current_path, width):
    file_list = os.listdir(current_path)
    for file in file_list:
        print(' ' * width, file)
        new_path = current_path + '/' + file
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)


def use_stat(file_path):
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                                 file_info.st_mode, file_info.st_mtime))
    from time import strftime
    from time import gmtime
    print(strftime('%Y-%m-%d %H:%M:%S',gmtime(file_info.st_mtime)))

if __name__ == '__main__':
    # use_rename()
    # use_dir_content()
    # scan_dir('.',0)
    use_stat('file1')
