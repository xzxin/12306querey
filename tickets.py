# -*- coding: utf-8 -*-
"""Train tickets query via command-line.
  Usage:
      tickets [-gdtkz] <from> <to> <date>

  Options:
      -h,--help   显示帮助菜单
      -g          高铁
      -d          动车
     -t          特快
     -k          快速
     -z          直达

 Example:
     tickets -gdt beijing shanghai 2016-08-25
 """
import requests
from docopt import docopt
from station import stations
# from pprint import pprint
from myprettytable import TrainCollection

class SelectTrain(object):

    def __init__(self):
        """
        获取命令行输入的参数
        """
        self.args = docopt(__doc__)#这个是获取命令行的所有参数，返回的是一个字典


    def cli(self):
        """command-line interface"""
        # 获取 出发站点和目标站点
        from_station = stations.get(self.args['<from>']) #出发站点
        to_station = stations.get(self.args['<to>']) # 目的站点
        leave_time = self._get_leave_time()# 出发时间

        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={0}&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT'.format(
        leave_time,from_station,to_station)# 拼接请求列车信息的Url


        # 获取列车查询结果
        r = requests.get(url,verify=False)
        traindatas = r.json()
        map = traindatas['data']['map']
        traindatas  = traindatas['data']['result'] # 返回的结果，转化成json格式，取出datas，方便后面解析列车信息用
        # 解析列车信息
        traintypes = self._get_traintype()
        views = TrainCollection(map,traindatas,traintypes)
        views.print_pretty()

    def _get_traintype(self):
        """
        获取列车型号，这个函数的作用是的目的是：当你输入 -g 是只是返回 高铁，输入 -gd 返回动车和高铁，当不输参数时，返回所有的列车信息
        """
        traintypes = ['-g','-d','-t','-k','-z']
        # result = []
        # for traintype in traintypes:
        #     if self.args[traintype]:
        #         result.append(traintype[-1].upper())

        trains = [traintype[-1].upper() for traintype in traintypes if self.args[traintype]]
        if trains:
            return trains
        else:
            return ['G','D','T','K','Z']

    def _get_leave_time(self):
        """
        获取出发时间，这个函数的作用是为了：时间可以输入两种格式：2016-10-05、20161005
        """
        leave_time = self.args['<date>']
        if len(leave_time) == 8:
            return '{0}-{1}-{2}'.format(leave_time[:4],leave_time[4:6],leave_time[6:])

        if '-' in leave_time:
            return leave_time


if __name__ == '__main__':
    cli = SelectTrain()
    cli.cli()