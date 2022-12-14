import time
import json
import re
from playwright.sync_api import sync_playwright
url = 'https://map.baidu.com/'
url_title = re.match(r'https:\/\/\w+?\.(\w+?)\.', url).group(1)


def 获取登录信息():
    with sync_playwright() as p:
        # 创建一个浏览器实例
        browser = p.chromium.launch(headless=False)
        # 创建含登录状态的浏览器上下文
        context = browser.new_context()
        # 创建一个page对象
        page = context.new_page()
        # 转到页面
        page.goto(url)
        # 获取登录状态
        input('登录之后按回车继续')
        storage = context.storage_state()
        with open(f"{url_title}_state.json", "w") as f:
            f.write(json.dumps(storage))


def 打开已登录页面(url_1):
    with sync_playwright() as p:
        # 创建一个浏览器实例
        browser = p.chromium.launch(headless=False)
        with open(f"{url_title}_state.json") as f:
            storage_state = json.loads(f.read())
        context = browser.new_context(storage_state=storage_state)
        page = context.new_page()
        page.goto(url_1)
        page.wait_for_timeout(1000000)


# 获取登录信息()
打开已登录页面(url_1=url)

