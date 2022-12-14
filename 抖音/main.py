import re
import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                  'Safari/537.36 Edg/107.0.1418.42',
    'cookie': 'd_ticket=282c9cd2bc855b29d58b61dc69a8a45a6f9fb; '
              's_v_web_id=verify_l8h0bm9a_5XsGdBTl_rqMv_4Oqn_BDHC_5BfwAEFGh3TI; '
              'passport_csrf_token=38a1b99de62b61b55ac2aec24527b2d7; '
              'passport_csrf_token_default=38a1b99de62b61b55ac2aec24527b2d7; '
              'n_mh=Fi1MMger22vK_lVs19db3hLXQ_-oWSdl6y28OEr0AQI; '
              'ttwid=1|Lr-F8P6YPwxNKF-CSVM2ZulRy1-74wBQsBBpMPaW17M|1665221971'
              '|e19df19fb3cbca01dc5acde8e0ba6fc357ec55d367d9304e04fdfdc815c73150; _tea_utm_cache_2018=undefined; '
              'download_guide="3/20221115"; strategyABtestKey=1668738958.302; live_can_add_dy_2_desktop="0"; '
              'douyin.com; csrf_session_id=673d83d934254451b42a9f9471c6c642; __ac_nonce=063774555004a53a7d445; '
              '__ac_signature=_02B4Z6wo00f01ingSGQAAIDCqeKyJ-U09n4pwEzAAOkdYlIM43U0e-1kcbhvnSUiDy4soCLhX2XW0'
              '.7f7vYyV0ueR5tVjrZqCyzJK4Fb2g70uWRl7MlYTiPRSgR4cTM.my00ptunbkqA29Hq53; '
              'passport_assist_user'
              '=Cj0dNDteNHdUYwMOb2f7qQgA6tSEesAQPuOV0bDOnnQV05vbrOjokuGm9wftfa__zNq1qFNCve8DjXieQJTFGkgKPPXwWkqZYxrHGgkKtpCdtSf4eEachw3t0TEACPdHseXrokz14JROcnTuirX40W0B3M1px7NzQQtds4mrrBCzxqENGImv1lQiAQM07Mrc; sso_uid_tt=de7168ef9e26fe074c46ae69cc57b713; sso_uid_tt_ss=de7168ef9e26fe074c46ae69cc57b713; toutiao_sso_user=2a57b30f9c4dc929d76e10c667544942; toutiao_sso_user_ss=2a57b30f9c4dc929d76e10c667544942; sid_ucp_sso_v1=1.0.0-KDJiYmE4OWI4NDQ5NjNlMTMwM2U0YWVmYjMwZjBmOWVmMjJiNDRlZjQKHQimxvvzmAMQ34rdmwYY7zEgDDCihrzhBTgCQO8HGgJsZiIgMmE1N2IzMGY5YzRkYzkyOWQ3NmUxMGM2Njc1NDQ5NDI; ssid_ucp_sso_v1=1.0.0-KDJiYmE4OWI4NDQ5NjNlMTMwM2U0YWVmYjMwZjBmOWVmMjJiNDRlZjQKHQimxvvzmAMQ34rdmwYY7zEgDDCihrzhBTgCQO8HGgJsZiIgMmE1N2IzMGY5YzRkYzkyOWQ3NmUxMGM2Njc1NDQ5NDI; odin_tt=d775010108562bcc06be0364b622bfb634813f754c94c9e5cb3cc3503dd17dd2fca5dfd51d5dc28eedc563a34e09302c4bae7e50cd3082c3145afd9c5186a8d2; sid_guard=a9fa0c65408204bbec255630feee4061|1668760927|5184000|Tue,+17-Jan-2023+08:42:07+GMT; uid_tt=b3e55e840de84093815c3788492b0e71; uid_tt_ss=b3e55e840de84093815c3788492b0e71; sid_tt=a9fa0c65408204bbec255630feee4061; sessionid=a9fa0c65408204bbec255630feee4061; sessionid_ss=a9fa0c65408204bbec255630feee4061; sid_ucp_v1=1.0.0-KGVkYTIyZmVlZjlhYTY3MTVhYzNmMWE5N2EzMzdkOTg1MDMwNTUyZTgKFwimxvvzmAMQ34rdmwYY7zEgDDgCQO8HGgJobCIgYTlmYTBjNjU0MDgyMDRiYmVjMjU1NjMwZmVlZTQwNjE; ssid_ucp_v1=1.0.0-KGVkYTIyZmVlZjlhYTY3MTVhYzNmMWE5N2EzMzdkOTg1MDMwNTUyZTgKFwimxvvzmAMQ34rdmwYY7zEgDDgCQO8HGgJobCIgYTlmYTBjNjU0MDgyMDRiYmVjMjU1NjMwZmVlZTQwNjE; FOLLOW_LIVE_POINT_INFO="MS4wLjABAAAAysaRRQy0XjSlDO-7VEj2Ee9VDxMWCMGYc03VbxBHc1s/1668787200000/0/0/1668761528477"; FOLLOW_NUMBER_YELLOW_POINT_INFO="MS4wLjABAAAAysaRRQy0XjSlDO-7VEj2Ee9VDxMWCMGYc03VbxBHc1s/1668787200000/0/1668760928478/0"; home_can_add_dy_2_desktop="1"; msToken=KBfQWV_Kc66doECliKta_T3ZErWp3-MBw7RaAgGBRX3KZHfUFhPjh04IuezxZ21cScFrAi_ZV4nWyWxo-VPYFvRhbogXpv8gp5sTgNOlN_FKumcE0O592KeEWWKvkdsC; msToken=mS09v9T1sutyfUMUX7jmVknAt_sYf_Js44EIdG7oy3wtmLYoX4SfAj72WosXBoS5MSguFvtTNTS0aVLsCydM0hq5D_9bGlEEOiRCv5-p-r2Z8OlvSbfL_Cevgqnb7yMe; tt_scid=JPIkBE8x5f3n5SAKjoZMLeSs4Ph3hAlBeZIj-SOYQtiASHbAnHPPKeZJp5gNPfJV9e50 '
}
user_homepage_url_1 = 'https://www.douyin.com/user/MS4wLjABAAAAjnqKAgfVsO7RRaNB3p53jC5s-KazYR0_4Rx1InbN8VY'
user_content_page_url_1 = 'https://www.douyin.com/video/7166829925113138467'
s = requests.Session()


# 基本api 把url转换为etree对象
def turn_url_etree_obj(url):
    """
    基本api 把url转换为etree对象

    :param url: 需要提取etree对象的url
    :return: etree对象
    """
    response = s.get(url=url, headers=headers)
    etree_object = etree.HTML(response.text)
    return etree_object


def homepage_to_content(user_homepage_url):
    """
    主页链接 -> 所有内容页链接

    :param user_homepage_url: 用户主页url
    :return: 内容页列表
    """
    user_homepage_etree_object = turn_url_etree_obj(user_homepage_url)
    content_urls: list = user_homepage_etree_object.xpath('//div/ul/li/a/@href')
    complete_urls = []
    for i in content_urls:
        i_1 = 'https://www.douyin.com' + i
        complete_urls.append(i_1)
    return complete_urls


def content_to_video(user_content_page_url):
    """
    内容页链接 -> 视频标题 和 视频流链接

    :param user_content_page_url: 用户内容页url
    :return: 视频标题, 视频链接
    """
    html = s.get(url=user_content_page_url, headers=headers)
    title = re.search('<title data-react-helmet="true">(.*?)抖音</title>', html.text).group(1)
    title = re.sub('[^\u4e00-\u9fa5]+', '', title)          # 去除特殊字符，只保留汉字，字母、数字
    video_url = re.findall('src%22%3A%22%2F%2F(v26.*?)%22%7D%2C%7B%22', html.text)[2]
    video_url = 'https://' + requests.utils.unquote(video_url)
    return title, video_url


def download(url, title):
    """
    下载保存(视频流链接 + 视频标题)
    """
    # 视频是二进制,需要这种下载办法
    video = s.get(url, headers=headers).content
    video_name = f"{title}.mp4"
    with open(video_name, 'wb') as f:
        f.write(video)
        f.flush()
    print("下载完成")


all_content_urls = homepage_to_content(user_homepage_url_1)
for content_url in all_content_urls:
    title_1, video_url_1 = content_to_video(content_url)
    print(title_1, '\n', video_url_1)
