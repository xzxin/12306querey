# -*- coding: utf-8 -*-
"""
Usage:
    test [-gdtkz] <from> <to> <date>

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
import docopt
args = docopt.docopt(__doc__)
print(args)