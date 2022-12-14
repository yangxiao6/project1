import requests

while True:
    address = input('\n请输入地址:\t')
    v = requests.get(f'https://restapi.amap.com/v3/geocode/geo?address={address}&output=json&key=66c3cd09c85e728fc3f769cbd05e63c0').json()
    v_1 = v['geocodes'][0]['location']
    t = requests.get(f'https://restapi.amap.com/v3/geocode/regeo?output=json&location={v_1}&key=66c3cd09c85e728fc3f769cbd05e63c0&radius=1000&extensions=all').json()

    baidu_v = requests.get(f'https://api.map.baidu.com/geocoding/v3/?address={address}&output=json&ak=323b7392b0a13f355693d2aceb628f84&callback=showLocation').text

    # for j, k in t['regeocode'].items():
    #     print(j, k)
    print('\t\t')
    print('省/直辖市/特别行政区:\t', t['regeocode']['addressComponent']['province'])
    print('地级市:\t', t['regeocode']['addressComponent']['city'])
    print('县/区/县级市:\t', t['regeocode']['addressComponent']['district'])
    print('乡镇/街道:\t', t['regeocode']['addressComponent']['township'])
    print('主路:\t', t['regeocode']['addressComponent']['streetNumber']['street'])
    print('主路门牌号:\t', t['regeocode']['addressComponent']['streetNumber']['number'])






