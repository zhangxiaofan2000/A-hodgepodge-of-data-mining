# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/9 13:56
# File : 区分助理.py
import re
import pandas as pd
import datetime
import os
import warnings
warnings.simplefilter('ignore')
print("#"*20)
print("请确保处理数据文件夹下的表名为"
      "\n总表.xlsx"
      "\n补单表.xlsx"
      "\n规格.csv")
print("#"*20)

try:
    start_time = datetime.datetime.now()
    current_time = datetime.datetime.now().strftime("%m.%d")


    path_supple = f'./区分结果/{current_time}处理结果/补单/'
    if not os.path.exists(path_supple):
        os.makedirs(path_supple)
    path_normal= f'./区分结果/{current_time}处理结果/正常发货/'
    if not os.path.exists(path_normal):
        os.makedirs(path_normal)


    order = pd.read_excel('./处理数据/总表.xlsx')
    order['订单编号'] = order['订单编号'].astype(str)
    order['联系手机'] = order['联系手机'].str.strip("'")

    shuadan = pd.read_excel('./处理数据/补单表.xlsx')

    new_order = pd.DataFrame(columns=order.columns)
    new_shuadan = pd.DataFrame(columns=order.columns)


    shuadan_index = []

    bianhao = shuadan['订单编号'].values
    for index, row in order.iterrows():
        if str(row['订单编号']) in bianhao:
            shuadan_index.append(index)

    new_shuadan = order.iloc[shuadan_index]

    shuadan_bianhao = new_shuadan['订单编号'].values
    gift = []
    for i in shuadan_bianhao:
        index = shuadan[shuadan['订单编号'] == i].index[0]
        gift.append(shuadan.iloc[index,5])
    new_shuadan.insert(1, '礼品', gift, True)

    #
    df1 = new_shuadan[new_shuadan['礼品'].str.contains('橙')]
    df2 = new_shuadan[new_shuadan['礼品'].str.contains('红薯')]
    df3 = new_shuadan[new_shuadan['礼品'].str.contains('紫薯')]
    df4 = new_shuadan[new_shuadan['礼品'].str.contains('猫')]
    df5 = new_shuadan[new_shuadan['礼品'].str.contains('布')]
    df6 = new_shuadan[new_shuadan['礼品'].str.contains('粉')]
    df7 = new_shuadan[new_shuadan['礼品'].str.contains('桶')]
    df8 = new_shuadan[~new_shuadan['礼品'].str.contains('橙|红薯|紫薯|猫|布|粉|桶')]
    # df8  = new_shuadan[~new_shuadan['礼品'].isin(['橙','红薯','紫薯','猫','布','粉','桶'])]
    writer = pd.ExcelWriter(f'{path_supple}/{current_time}补单发货.xlsx', engine='openpyxl')
    new_shuadan.to_excel(writer, sheet_name='sheet1', index=False)
    df1.to_excel(writer, sheet_name='橙', index=False)
    df2.to_excel(writer, sheet_name='红薯', index=False)
    df3.to_excel(writer, sheet_name='紫薯', index=False)
    df4.to_excel(writer, sheet_name='猫耳框', index=False)
    df5.to_excel(writer, sheet_name='收纳桶', index=False)
    df6.to_excel(writer, sheet_name='螺螂粉', index=False)
    df7.to_excel(writer, sheet_name='毛毡桶', index=False)
    df8.to_excel(writer, sheet_name='其他', index=False)

    writer.save()
    writer.close()
    columns = ['订单编号','收货人姓名','联系手机','收货地址']
    df1[columns].to_excel(f'{path_supple}/{current_time}橙.xlsx', index=False)
    df2[columns].to_excel(f'{path_supple}/{current_time}红薯.xlsx', index=False)
    df3[columns].to_excel(f'{path_supple}/{current_time}紫薯.xlsx', index=False)
    df4[columns].to_excel(f'{path_supple}/{current_time}猫耳框.xlsx', index=False)
    df5[columns].to_excel(f'{path_supple}/{current_time}收纳桶.xlsx', index=False)
    df6[columns].to_excel(f'{path_supple}/{current_time}螺螂粉.xlsx', index=False)
    df7[columns].to_excel(f'{path_supple}/{current_time}毛毡桶.xlsx', index=False)
    df8[columns].to_excel(f'{path_supple}/{current_time}其他.xlsx', index=False)




    order.drop(shuadan_index, inplace=True)


    # order = order.reindex(range(len(order)))
    order.to_excel(f'{path_normal}/正常发货.xlsx', index=False)



    order_guige = pd.read_csv('./处理数据/规格.csv',encoding="gbk")
    order_guige['主订单编号'] = order_guige['主订单编号'].apply(lambda x: x.strip('="'))


    specification = order['订单编号'].values
    properties = []
    weight = []
    length=[]
    for i in specification:
        try:
            index = order_guige[order_guige['主订单编号'] == i].index[0]
            p = order_guige.loc[index,"商品属性"]
            properties.append(p)
            weight.append(int(re.search(r'\d+斤',p).group(0)[:-1]))
        except:
            # print(f"\033[33m订单{i}未找到规格,请更新规格表。\033[0m")
            print(f"订单{i}未找到规格,请更新规格表。")

            properties.append("无")
            weight.append(0)

    for i in specification:
        try:
            index = order_guige[order_guige['主订单编号'] == i].index[0]
            p = order_guige.loc[index,"商品属性"]
            length.append(int(re.search(r'\d{2,3}mm',p).group(0)[:-2]))
        except:
            length.append(0)

    order.insert(1, "商品属性", properties, True)
    order.insert(2, "斤数", weight, True)
    order.insert(3, "果径", length, True)

    order.sort_values(by=['斤数', '果径'], ascending=[False, False], inplace=True)

    columns = ['订单编号','收货人姓名','联系手机','收货地址','商品属性']

    grouped = order.groupby('宝贝标题 ')
    for name, group in grouped:
        new_df = group.reset_index(drop=True)
        new_df[columns].to_excel(f"{path_normal}/{current_time}{name}.xlsx", index=False)

    # print(f"\033[1;32m 运行成功!耗时{datetime.datetime.now()-start_time}秒\033[0m")
    print(f"运行成功!耗时{datetime.datetime.now()-start_time}秒")

except :
    # print("\033[31m运行失败！\033[0m")
    print("运行失败！")


os.system('pause')



