import os
import logging
import formats

logging.basicConfig(level=logging.INFO, filename='sorting.log', filemode='w', format='%(levelname)s - %(message)s')
def scaning(parent):
    files = list(filter(os.path.isfile, os.listdir()))
    logging.info("{0} : {1}".format(os.getcwd(), files))
    directory = parent + '\sorting.db'
    for file in files:
        format = ''
        for i in range(len(file) - 1, 0, -1):
            if file[i] == '.':
                break
            format += file[i]
        else:
            continue
        format = format[::-1]
        logging.info("{0} : {1} -> {2}".format(os.getcwd(), file, format))
        type = formats.searchtype(format, directory)
        logging.info("{0} --> {1}".format(format, type))
        if type:
            type = type[0]
            storage = formats.takestorage(type, directory)
            logging.info("{0} премещен в {1}".format(file, storage))
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
    parent = os.getcwd()
    directory = str(input('Какую директорию отсортировать:'))
    while True:
        if len(directory) == 0 :
            directory = parent
            break
        if os.path.isdir(directory):
            break
        else:
            directory = str(input('Неверно указан путь \n. Какую директорию отсортировать:'))
    os.chdir(directory)
    scaning(parent)

start()