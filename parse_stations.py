#coding=utf-8

import requests
import re
from pprint import pprint


def get_stations():
    #@cqb|重庆北|CUW|chongqingbei|cqb|6
    url = r'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9042'
    response = requests.get(url,verify=False)
    pattern = re.compile('([A-Z]{3})\|([a-z]+)')
    items = dict(re.findall(pattern,response.text))
    stations = dict(zip(items.values(),items.keys()))
    pprint(stations,indent=4)
get_stations()