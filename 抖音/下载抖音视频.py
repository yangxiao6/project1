import requests
import json
import re

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
}


def download(url):
    """
    下载抖音无水印视频
    """

    # 视频是二进制,需要这种下载办法
    video = requests.get(url, headers=headers).content
    video_name = "douyin.mp4"
    with open(video_name, 'wb') as f:
        f.write(video)
        f.flush()
    print("下载完成")


if __name__ == '__main__':
    # 抖音链接
    url = 'http://v26-web.douyinvod.com/9fa961c2601fc4aff647c134595a9f74/637764d4/video/tos/cn/tos-cn-ve-15c001-alinc2/cf86f3384d9849a096b878e9cc4a1cf9/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1925&bt=1925&cs=0&ds=3&ft=pP-tGp22Hjnl9KJB8yqsd.3a2C98lcvNmq2yWHruJd&mime_type=video_mp4&qs=0&rc=N2lnZTU7Njw4NjY2ZzQ3O0BpamozbmY6Zm04ZzMzNGkzM0A2YV8xMi8uNS0xYl5eLzYxYSNecGhucjRvbGFgLS1kLWFzcw%3D%3D&l=021668765374443fdbddc02002304290c41b61660000035f513ff&btag=8000'
    download(url)
