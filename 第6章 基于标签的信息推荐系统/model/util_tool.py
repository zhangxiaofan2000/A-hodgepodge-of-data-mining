#!/usr/bin/python
#coding:utf-8
from pathlib import Path

def file_exist(filename):
    my_file = Path(filename)
    if my_file.is_file():
        return True
    return False

def get_file_list(file_name):
    if file_exist(file_name) == False: return None
    
    with open(file_name,'r',encoding = 'utf-8') as file:
        return list([line.strip() for line in file])
    return None

def writeList2File(full_file_name,list,mode='w'):
    thefile = open(full_file_name, mode,encoding='utf-8')
    for item in list:
        thefile.write("%s\n" % item)
    thefile.close()


def isChinese(char):
    if char == None:
        return False
    if u'\u4e00' <= char <= u'\u9fff':
        return True
    return False

def replace_punc(check_str,old_punc,new_punc):
    if check_str == None:
        return ""
    
    index =0
    loop_count = len(check_str)
    while index < loop_count:
        ch = check_str[index]
        if ch == old_punc:
            left_ch = check_str[index-1] if index>0 else None
            right_ch = check_str[index+1] if index < loop_count-1 else None
            if isChinese(left_ch) or isChinese(right_ch):#原来是符号左右两边都是中文才作替换，现在改为：只要左侧或右侧为中文就替换
                check_str = check_str[:index] + new_punc +check_str[index+1:]
        index +=1
        loop_count = len(check_str)
    
    return check_str
