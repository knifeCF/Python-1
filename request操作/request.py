# -*- coding: utf-8 -*-
import requests
import re
import csv
# 程序主入口
if __name__ == "__main__":
    """模仿浏览器，请求api信息"""
    url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2021-03-03&ed=2022-03-03&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.006363098283545421'
    headers = {
        'Cookie': '_adsame_fullscreen_16928=1; qgqp_b_id=261417d1c0ebcfa96bd3a5b0edb6a81c; ASP.NET_SessionId=lonmp3ewl0lvcbzlzx4hsndt; st_si=25075116710553; st_pvi=38462203580371; st_sp=2021-08-18%2015%3A36%3A52; st_inirUrl=http%3A%2F%2Ffund.eastmoney.com%2Fcompany%2Fdefault.html; st_sn=1; st_psi=20220303182533717-112200312936-7108151575; st_asi=delete; _adsame_fullscreen_18503=1; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=null; EMFUND0=null; EMFUND9=03-03 18:26:43@#$%u91D1%u4FE1%u6C11%u5174%u503A%u5238A@%23%24004400',
        'Host': 'fund.eastmoney.com',
        'Referer': 'http://fund.eastmoney.com/data/fundranking.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
#发送请求
    request = requests.get(url, headers=headers)
#获取数据
    data = request.text
    print(data)
#解析数据
data_str = re.findall('\[(.*?)\]',data)[0]
print(eval(data_str))
