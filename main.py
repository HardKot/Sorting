import os
from listtype import types

def bisearch(arr, name):
    if arr[len(arr) // 2] < name:
        return bisearch(arr[:len(arr) // 2], name)
    if arr[len(arr) // 2] > name:
        return bisearch(arr[len(arr) // 2 :], name)
    if arr[len(arr) // 2] == name:
        return True
    else:
        return False

def typewriter(format):
    for type in types:
        if types.get(type).count(format):
            return type
    else:
        return False

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
        type = typewriter(format)
        if type:
            os.system(r'move "{0}\{1}" c:\users\{2}\{3}'.format(os.getcwd(),
                                                                file,
                                                                os.getlogin(),
                                                                type))

scaning()
