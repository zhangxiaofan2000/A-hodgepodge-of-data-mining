# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/23 10:57
# File : network.py
import os
import pickle
from mpl_toolkits.basemap import Basemap

import pandas as pd
import networkx as nx
import requests
from matplotlib import pyplot as plt
from shapely.geometry import Point, LineString

from pathplanning.amapRoutePlanner import amapRoutePlanner

#支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def create_weighted_directed_graph(excel_path, key):
    # 读取 Excel 文件
    df = pd.read_excel(excel_path)

    # 创建空的有向图
    G = nx.DiGraph()

    # 将每个节点添加到图中
    for _, row in df.iterrows():
        node = row['名称']
        G.add_node(node, pos=(row['经度'],row['纬度']),latitude=row['纬度'], longitude=row['经度'])

    # 将每个边添加到图中
    rp = amapRoutePlanner(key)
    for _, row in df.iterrows():
        source = row['名称']
        for _, row2 in df.iterrows():
            target = row2['名称']
            if source != target:
                # 如果两个节点不相同，则添加边
                origin = f"{row['经度']},{row['纬度']}"
                destination = f"{row2['经度']},{row2['纬度']}"
                params = {
                    "origin": origin,
                    "destination": destination,
                    "key": key,
                }
                url = "https://restapi.amap.com/v3/direction/driving?"
                data = rp.send_request(url, params)
                if data is not None:
                    route_info = rp.get_route_info(data)
                    if route_info is not None:
                        distance = route_info['distance']
                        G.add_edge(source, target, weight=distance)

    return G



# 保存有向图为CSV文件
def save_graph_csv(G, csv_path):
    df = pd.DataFrame(G.edges(data=True), columns=['source', 'target', 'distance'])
    df['distance'] = df['distance'].apply(lambda x: x['weight'])
    df.to_csv(csv_path, index=False)


# 读取CSV文件为有向图
def read_graph_csv(csv_path):
    df = pd.read_csv(csv_path)
    G = nx.from_pandas_edgelist(df, 'source', 'target', ['distance'], create_using=nx.DiGraph())
    return G



# 保存图
def save_graph(graph, filename):
    with open(filename, 'wb') as f:
        pickle.dump(graph, f)

# 加载图
def load_graph(filename):
    with open(filename, 'rb') as f:
        graph = pickle.load(f)
    return graph


# 创建图
def creat():
    G = create_weighted_directed_graph('data/数据demo(1).xlsx', '4aef85d38f43ba0c108c516789c24c67')
    path = "./graph/"
    if not os.path.exists(path):
        os.makedirs(path)
    # # 保存有向图为CSV文件
    save_graph_csv(G, './graph/graph.csv')
    # # 保存有向图的所有信息
    save_graph(G, './graph/graph.pkl')

def plot_graph():
    G = load_graph('./graph/graph.pkl')
    # 获取节点位置
    pos = nx.get_node_attributes(G, 'pos')
    # 获取边权重
    weights = nx.get_edge_attributes(G, 'weight')
    # 绘制图
    plt.figure(figsize=(15, 15),dpi=200)
    nx.draw_networkx(G, pos, with_labels=True, node_size=200, font_size=8, node_color='lightblue', edge_color='gray', width=2, edge_cmap=plt.cm.Blues)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_size=8)
    plt.axis('off')
    plt.savefig("./graph/graph_on_map.png")



def plot_graph_on_map():
    G = load_graph('./graph/graph.pkl')
    # 获取节点位置
    pos = nx.get_node_attributes(G, 'pos')
    # 获取边权重
    weights = nx.get_edge_attributes(G, 'weight')
    plt.figure(figsize=(15, 15),dpi=200)

    # 获取地图范围
    lats = [pos[node][1] for node in pos]
    lons = [pos[node][0] for node in pos]
    lat_min, lat_max = min(lats), max(lats)
    lon_min, lon_max = min(lons), max(lons)
    map = Basemap(llcrnrlon=lon_min-0.05, llcrnrlat=lat_min-0.05, urcrnrlon=lon_max+0.05, urcrnrlat=lat_max+0.05, projection='merc', resolution='h')
    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color='lightgray', lake_color='aqua')
    map.drawmapboundary(fill_color='aqua')

    # 绘制节点和边
    nx.draw_networkx(G, pos, with_labels=True, node_size=200, font_size=8, node_color='lightblue', edge_color='gray', width=2, edge_cmap=plt.cm.Blues)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_size=8)

    # 保存图像
    plt.savefig("./graph/graph_on_map2.png")

plot_graph_on_map()
# plot_graph()