'''
    #利用python读取word文档，先读取段落
'''
import os
from docx import Document
import difflib
from tqdm import tqdm
import pandas as pd

def word_find(file_name,name):

    #打开word文档
    document = Document(f'{path}\{file_name}')

    #获取所有段落
    all_paragraphs = document.paragraphs
    #打印看看all_paragraphs是什么东西

    #是列表就开始循环读取
    all_list = []
    for paragraph in all_paragraphs:
        #打印每一个段落的文字
        all_list.append(paragraph.text)



    data = difflib.get_close_matches(name, all_list, cutoff=0.1)

    # index_key = [for ]all_list.index(data) + 1
    print(file_name,data)
    # print(index_key)
    return all_list







def find_table(file_name,name):
    '''
    查找 file_name 内 含有name的表格
    :param file_name: word 的文件名
    :param name: 要找的字段
    :return: file_name
    '''
    document = Document(f'{path}\{file_name}')


    for table in document.tables:
        for i,row in enumerate(table.rows):
            if i==0:
                for cell in row.cells:
                    if cell.text == name:
                        # print(file_name)
                        return file_name
    return 'not find'

def find_all_file(path,name):
    '''
    查找表格内含有 '排放浓度' 的所有文件
    :param path:查找路径
    :return:
    '''

    filelist = []
    for file_name in tqdm(os.listdir(path)):
        ans = find_table(file_name, name)
        if ans !='not find':
            filelist.append(ans)
    return filelist

def find_table_return_table(file_name,name):
    '''
    查找 file_name 内 含有name的表格
    :param file_name: word 的文件名
    :param name: 要找的字段
    :return: table
    '''
    document = Document(f'{path}\{file_name}')
    tables=[]
    flag=0
    columns_num=0
    for table in document.tables:

        if flag == 0:

            for i, row in enumerate(table.rows):
                if i == 0:
                    for cell in row.cells:
                        if cell.text == name:
                            flag = 1
                            tables.append(table)

                columns_num = len(row.cells)



        elif flag == 1 and columns_num==len(table.columns):

            for row in table.rows:
                for cell in row.cells:
                    tables.append(table)
            columns_num = len(row.cells)


    return  tables
def word_table_to_excel(tables,output):
    '''
    word 表格转换为 excel
    :param table: 
    :param output: 输出路径
    :return: 
    '''
    table_list=[]
    for table in tables:
        for row in table.rows:
            row_list = []
            for cell in row.cells:
                row_list.append(cell.text)
            table_list.append(row_list)

    df = pd.DataFrame(table_list[1:],columns=table_list[0])
    df.to_excel(output,index=False)
    return df


if __name__ =="__main__":

    path = 'G:\proprocess\data\年报WORD'
    path = 'G:\proprocess\data\年报WORD9'

    output_path = 'G:\proprocess\data\output'

    # for file_name in os.listdir(path):
    #     word_find(file_name, '环境保护')
    # all_list = word_find('000028-国药一致-2020年年度报告.docx', '废气监测方案')

    # # 寻找表头含有 '排放浓度' 的文件
    # filelist = find_all_file(path,'排放浓度')

    #
    for file_name in tqdm(os.listdir(path)):
        tables = find_table_return_table(file_name,'排放浓度')

        if len(tables)>0:
            word_table_to_excel(tables, f'{output_path}\{file_name}.xlsx')
