def read_conf():
    file = open('file6', 'r+', encoding='utf-8')
    text = file.read()
    print(text)
    my_dict = eval(text)
    print(my_dict['ip'])


if __name__ == '__main__':
    read_conf()
