# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/23 10:57
# File : network.py
import pandas as pd
import networkx as nx

from pathplanning.amapRoutePlanner import amapRoutePlanner
'''
生成换电充电网络
'''

def create_weighted_directed_graph(excel_path, key):
    # 读取 Excel 文件
    df = pd.read_excel(excel_path)

    # 创建空的有向图
    G = nx.DiGraph()

    # 将每个节点添加到图中
    for _, row in df.iterrows():
        node = row['名称']
        node_type = row['类型']
        G.add_node(node, type=node_type)

    # 将每个边添加到图中
    rp = amapRoutePlanner(key)
    for _, row in df.iterrows():
        source = row['名称']
        source_type = row['类型']
        for _, row2 in df.iterrows():
            target = row2['名称']
            target_type = row2['类型']
            if source != target and source_type != '充电站' and target_type != '充电站':
                # 如果两个节点不相同，并且都不是充电站，则添加边
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


def save_to_excel(G, file_path):
    nodes = [{'id': n, 'type': G.nodes[n]['type']} for n in G.nodes()]
    edges = [{'source': e[0], 'target': e[1], 'distance': G.edges[e]['weight']} for e in G.edges()]

    node_df = pd.DataFrame(nodes)
    edge_df = pd.DataFrame(edges)

    writer = pd.ExcelWriter(file_path)
    node_df.to_excel(writer, sheet_name='Nodes', index=False)
    edge_df.to_excel(writer, sheet_name='Edges', index=False)
    writer.save()


G = create_weighted_directed_graph('数据demo(1).xlsx', '4aef85d38f43ba0c108c516789c24c67')
save_to_excel(G, 'result.xlsx')

