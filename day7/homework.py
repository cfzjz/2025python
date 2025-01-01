import os


def scan_dir(current_path,width):
    file_list=os.listdir(current_path)
    for i in file_list:
        print(' '*width,i)
        new_path=current_path+'/'+i
        if os.path.isdir(new_path):
            scan_dir(new_path,width+4)

if __name__ == '__main__':
    scan_dir('.',0)
