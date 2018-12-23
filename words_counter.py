#!/usr/bin/python3
"""
This is cli utility analogous to wc on linux that counts lines, words and bytes.
You can use it by writing filenames as arguments.
It is also possible to output only number of lines(-l), words(-w) or bytes(-c).
Furthermore, you can use sdtin instead of real files.
"""
import sys
import os


def get_files_options(argv):
    text_files = set()
    args = set()
    for arg in argv:
        if arg.startswith('-'):
            if arg not in ('-l', '-w', '-c'):
                raise Exception(f'No such option {arg}')
            args.add(arg)
        else:
            text_files.add(arg)
    return text_files, args


def calculate(input_file):
    count_words = 0
    count_lines = 0
    cont_bytes = 0
    for line in input_file:
        cont_bytes += len(line.encode())
        count_words += len(line.split())
        count_lines += 1
    return count_lines, count_words, cont_bytes


def show_info(stats, argv):
    show_all = True
    if '-l' in argv:
        print(stats[0], end=' ')
        show_all = False
    if '-w' in argv:
        print(stats[1], end=' ')
        show_all = False
    if '-c' in argv:
        print(stats[2], end=' ')
        show_all = False
    if show_all:
        print(*stats, end=' ')


if __name__ == '__main__':
    file_names, options = get_files_options(sys.argv[1:])
    if not file_names:
        files = [sys.stdin]
    else:
        files = []
        for name in file_names:
            if os.path.isfile(name):
                files.append(open(name))
            else:
                raise Exception(f'{name} is not a file')
    for file in files:
        info = calculate(file)
        show_info(info, options)
        print(f':{file.name}')
        file.close()
