# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/23 10:34
# File : main.py
from pathplanning.amapRoutePlanner import amapRoutePlanner

if __name__ == "__main__":
    origin = "116.481028,39.989643"
    destination = "116.434446,39.90816"
    key = "4aef85d38f43ba0c108c516789c24c67"

    route_planner = amapRoutePlanner(key)
    result = route_planner.run(origin, destination)

