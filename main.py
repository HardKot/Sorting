import os
import formats

def scaning():
    files = list(filter(os.path.isfile, os.listdir()))
    for file in files:
        format = ''
        for i in range(len(file) - 1, 0, -1):
            if file[i] == '.':
                break
            format += file[i]
        else:
            continue
        format = format[::-1]
        type = formats.searchtype(format)
        if type:
            type = type[0]
            storage = formats.takestorage(type)
            os.system(r'move "{0}\{1}" {2}'.format(os.getcwd(), file, storage))

def start():
    if os.path.getsize('sorting.db') == 16384 and False:
        for type in formats.taketype():
            type = type[0]
            storge = str(input('Введите куда будут отправляться файлы типа {}: '.format(type)))
            if len(storge):
                formats.addstorage(type, storge)
            else:
                storage = r"C:\Users\{1}\{2}".format(os.getlogin(), type)
                formats.addstorage(type, storge)
    scaning()

start()