"""需求: 找到对应的行数的  详细地址(百度用)   /     poiid (高德用)
完整目标:  重新打开对应地图工具,   可以直接套到别的py文件中用
"""
# 导入openpyxl库
import openpyxl
# 打开文件
import requests

wb = openpyxl.load_workbook('算法挖掘数据样本_map_tool.xlsx')       # workbook,工作簿
ws = wb['王二']                                                   # worksheet,工作表
poiid_column = 'a'                                               # poiid所在列
reference_point_column = 'e'                                     # 参考位置所在列
reference_fence_column = 'f'                                     # 参考围栏所在列
query_row = '21'                                                 # 查询的行数

# 获取poiid
poiid = ws[f'{poiid_column}{query_row}'].value

# 高德地图url
amap_url = f'https://ditu.amap.com/place/{poiid}'


# 百度地图url
def 获取带市区的aoi名字(poi_id):
    URL = 'https://restapi.amap.com/v5/place/detail?parameters'
    params = {'key': '66c3cd09c85e728fc3f769cbd05e63c0', 'id': poi_id}
    HTML = requests.get(url=URL, params=params)
    数据 = HTML.json()
    if 数据['pois']:
        名字 = 数据['pois'][0]['name']
        城市 = 数据['pois'][0]['cityname']
        县区 = 数据['pois'][0]['adname']
        经纬度 = 数据['pois'][0]['location']
        带地区的aoi名字 = 城市 + 县区 + 名字
        带地区的aoi名字 = 带地区的aoi名字.strip()
    else:
        带地区的aoi名字 = ''
    return 带地区的aoi名字


address = 获取带市区的aoi名字(poiid)
baidu_url = f'http://api.map.baidu.com/geocoder?address={address}&output=html&src=webapp.baidu.openAPIdemo'
