#coding=utf-8

from prettytable import PrettyTable

class TrainCollection(object):
    """
    解析列车信息
    """
    # 显示车次、出发/到达站、 出发/到达时间、历时、一等坐、二等坐、软卧、硬卧、硬座
    header = '序号 车次 出发站/到达站 出发时间/到达时间 历时 商务座 一等座 二等座 软卧 硬卧 硬座 无座'.split()
    def __init__(self,map,rows,traintypes):
        self.rows = rows
        self.traintypes = traintypes
        self.map = map

    def _get_duration(self,row):
        """
        获取车次运行的时间
        """
        duration = row.get('lishi').replace(':','小时') + '分'

        if duration.startswith('00'):
            return duration[4:]
        elif duration.startswith('0'):
            return duration[1:]

        return duration

    @property
    def trains(self):
        result = []
        flag = 0
        for row in self.rows:
            result_list = row.split("|")
            train_no = result_list[3]
            from_station = result_list[6]
            temp = self.map.get(from_station)
            if temp is not None:
                from_station = temp
            to_station = result_list[7]
            temp = self.map.get(to_station)
            if temp is not None:
                to_station = temp
            start_time = result_list[8]
            arrive_time = result_list[9]
            duration_time = result_list[10]
            swz_num = result_list[20]
            ydz_num = result_list[31]
            edz_num = result_list[30]
            rw_num = result_list[23]
            yw_num = result_list[28]
            yz_num = result_list[29]
            wz_num = result_list[26]


            if True:#row['station_train_code'][0] in self.traintypes:
                flag += 1
                train = [
                    # 序号
                    flag,
                    # 车次
                    train_no,
                    # 出发、到达站点
                    '/'.join([from_station,to_station]),
                    # 成功、到达时间
                    '/'.join([start_time,arrive_time]),
                    # duration 时间
                    duration_time,
                    # 商务座
                    swz_num,
                    # 一等座
                    ydz_num,
                    # 二等座
                    edz_num,
                    # 软卧
                    rw_num,
                    # 硬卧
                    yw_num,
                    # 硬座
                    yz_num,
                    # 无座
                    wz_num
                ]
                result.append(train)

        return result

    def print_pretty(self):
        """打印列车信息"""
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)

        print(pt)


if __name__ == '__main__':
    t = TrainCollection()
