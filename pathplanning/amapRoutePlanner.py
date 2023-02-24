# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/23 10:31
# File : RoutePlanner.py
import requests

class amapRoutePlanner:
    def __init__(self, key):
        self.key = key

    def send_request(self, url: str, params: dict) -> dict:
        '''
        该函数用于发送HTTP请求并获取响应结果，返回响应结果的JSON数据。参数url表示请求的URL，params表示请求参数，类型为字典。如果请求出错，该函数将返回None。
        :param url:
        :param params:
        :return:
        '''
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # 检查响应状态码是否为200，否则抛出异常
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print("发送请求时出错:", e)
            return None
        except ValueError as e:
            print("分析响应数据时出错:", e)
            return None

    def get_route_info(self, data: dict) -> dict:
        '''
        该函数用于分析从高德地图API返回的路径规划结果，返回一个字典，包含行驶距离、预计行驶时间、策略和路径规划步骤等信息。参数data表示从API获取到的JSON数据。如果路径规划失败，该函数将返回None。
        :param data:
        :return:
        '''
        try:
            if data["status"] == "1":
                route = data["route"]
                paths = route['paths']
                path = paths[0]
                distance = path["distance"]  # 行驶距离，单位：米
                duration = path["duration"]  # 预计行驶时间，单位：秒
                strategy = path["strategy"]  # 策略
                steps = path["steps"]  # 路径规划步骤
                return {
                    "distance": distance,
                    "duration": duration,
                    "strategy": strategy,
                    "steps": steps
                }
            else:
                print("路径规划失败")
                return None
        except KeyError as e:
            print("分析响应数据时出错:", e)
            return None

    def run(self, origin, destination):
        '''
        该函数用于运行路径规划程序并返回规划结果。参数origin和destination分别表示出发点和目的地的经纬度，格式为字符串。函数会首先构造API请求的URL和参数，然后调用send_request方法发送HTTP请求获取响应数据，最后解析响应数据并返回规划结果。如果规划失败，该函数将返回None。
        :param origin:
        :param destination:
        :return:
        '''
        url = "https://restapi.amap.com/v3/direction/driving?"
        params = {
            "origin": origin,
            "destination": destination,
            "key": self.key,
        }
        data = self.send_request(url, params)
        if data:
            return self.get_route_info(data)
        else:
            return None