# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/23 9:25
# File : Truck_route_planning.py


'''
开发文档 路径规划1.0
https://lbs.amap.com/api/webservice/guide/api/direction

开发文档 路径规划2.0
https://lbs.amap.com/api/webservice/guide/api/newroute

错误码
https://developer.amap.com/api/webservice/guide/tools/info
'''
import json
import requests

from pathplanning import RoutePlanner

# 出发点和目的地经纬度
origin = "116.481028,39.989643"
destination = "116.434446,39.90816"
key= "4aef85d38f43ba0c108c516789c24c67"

# 构造请求URL
# url = "	https://restapi.amap.com/v5/direction/driving?"
url = "	https://restapi.amap.com/v3/direction/driving?"
params = {
    "origin": origin,
    "destination": destination,
    "key": key,
}

response_data = RoutePlanner.send_request(url,params)



response_data = send_request(url,params)
route_info = get_route_info(response_data)