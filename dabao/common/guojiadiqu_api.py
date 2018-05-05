# coding:utf-8
import requests
import re
import json


# 定义一个国家地区的类，包好返回国家/地区数据、省市数据、县/区数据
class Guojiadiqu_api():
    def __int__(self):
        print("初始化数据")

    # 返回国家数据
    def Country(self):
        url = "http://192.168.14.228:1337/api/v1/cities/%2f/0"
        r = requests.get(url)
        res = r.json()['cities'][0] # 提取keys信息
        zhi = {'id','cityCode','name'}  # 提取需要的返回值
        guojia = { key:value for key,value in res.items() if key in zhi} # 使用字典格式输出
        return guojia

    # 返回省市数据
    def city(self):
        url1 = "http://192.168.14.228:1337/api/v1/cities/%2f/1"
        r1 = requests.get(url1)
        res1 = r1.json()['cities'][0] # 提取keys信息
        zhi1 = {'id','cityCode','name'}  # 提取需要的返回值
        city = { key:value for key,value in res1.items() if key in zhi1} # 使用字典格式输出
        return city

    # 返回县/区数据
    def area(self):
        url1 = "http://192.168.14.228:1337/api/v1/cities/%2f/1"
        r1 = requests.get(url1)
        res2 = r1.json()['cities'][0] # 提取keys信息
        zhi2 = {'id','cityCode','name'}  # 提取需要的返回值
        area = { key:value for key,value in res2.items() if key in zhi2} # 使用字典格式输出
        return area


#检测一下封装类的方式是否都正常
# if __name__ == "__main__":
#     a = Guojiadiqu_api()  # 类的实例化
#     print(a.Country())
#     print(a.city())
#     print(a.area())
