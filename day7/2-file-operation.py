def open_r():
    file = open('file1', encoding='utf-8')

    text = file.read()
    print(text)
    file.close()


def open_wr():
    f = open('file1', mode='w+', encoding='utf-8')

    f.write('python\n')
    f.write('好')

    f.close()


def open_rw():
    f = open('file1', mode='r+', encoding='utf-8')
    f.write('aaa')
    f.close()


def open_a():
    f = open('file1', mode='a', encoding='utf-8')
    f.write('aaa')
    f.close()


def use_readline():
    f = open('file1', mode='r', encoding='utf-8')
    while True:
        text = f.readline()

        if not text:
            break

        print(text, end="")
    f.close()


def use_copy_file():
    file_read = open('file1', encoding='utf-8')
    file_write = open('file2', mode='w', encoding='utf-8')
    file_write2 = open('file3', mode='w', encoding='utf-8')

    text = file_read.read()
    file_write.write(text)

    file_read.seek(0,0)
    while True:
        text = file_read.readline()
        if not text:
            break
        file_write2.write(text)

    file_read.close()
    file_write.close()
    file_write2.close()

def use_seek():
    file=open('file1',encoding='utf-8')
    file.seek(8,0)
    text=file.read(5)
    print(text)
    file.close()

def use_seek_b():
    file=open('file4',mode='rb+')
    file.seek(5,1)
    file.seek(-2,1)
    file.seek(-3,2)
    bytestream=file.read()
    print(bytestream)
    file.close()

def copy_file():
    file_read=open('test.jpg',mode='rb+')
    file_write=open('test_copy.jpg',mode='wb')
    c=file_read.read()
    file_write.write(c)
    file_write.close()
    file_read.close()
def edit_picture():
    f=open('test_copy.jpg',mode='rb+')
    f.seek(10,0)
    text=f.read(1)
    text=int.from_bytes(text,byteorder='big')
    text=(~text)&0xff
    text=text.to_bytes(1,byteorder='big')

    f.seek(10,0)
    f.write(text)
    f.close()

if __name__ == '__main__':
    # open_r()
    # open_rw()
    # open_a()
    # use_readline()
    # use_copy_file()
    # use_seek()
    use_seek_b()
    # copy_file()
    # edit_picture()
