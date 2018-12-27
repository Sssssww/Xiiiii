"""
CSV(command-separated-vlaue)逗号分割符
CSV文件使用是由任意的数据记录组成,记录间某种换行符分割,符号记录有换行符组合


文件可以用Ecel格式打开 用于数据分析
"""


import csv
headers = ['ID','UserName','Age''Country']

rows = [
    ('1001','XiaoLiu',18,'US'),
    ('1002','DaHu',99,'UK'),
    ('1003','MaLaoShi',100,'CH'),
    ('1004','QianXin',77,'JP')
]

with open('test.csv','w') as f :
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)