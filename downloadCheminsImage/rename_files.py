# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/28 13:56
# File : rename_files.py
import os

def rename_files(path, log_file):
    with open(log_file, 'w', encoding='utf-8') as f:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                # Get the full path of the file
                full_path = os.path.join(dirpath, filename)
                # Rename the file by replacing any Chinese characters or spaces with underscores
                new_filename = ''.join(c if (ord(c) < 128 and c != ' ') else '' for c in filename)
                os.rename(full_path, os.path.join(dirpath, new_filename))
                # Write the old and new file names to the log file
                f.write(f'{filename}\t{new_filename}\n')

if __name__ == '__main__':
    # Replace 'path/to/folder' with the path to the folder you want to process
    folder_path = 'G:\proprocess\downloadCheminsImage\压缩后传感器图片'
    # Replace 'path/to/log.txt' with the path to the log file you want to create
    log_path = 'G:\proprocess\downloadCheminsImage\log.txt'
    rename_files(folder_path, log_path)

