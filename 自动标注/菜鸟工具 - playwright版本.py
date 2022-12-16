import webbrowser

from playwright.sync_api import sync_playwright
import json
import openpyxl
import requests


# xlsx基础操作
class OperateXlsx:
    def __init__(self):

        self.xlsx_address = '算法挖掘数据样本9-王二-00-00.xlsx'
        self.sheet_name = '王二'
        self.poi_id_column = 'a'
        self.poi_name_column = 'b'
        self.reference_point_column = 'e'
        self.reference_fence_column = 'f'
        self.correct_fence_column = 'j'
        self.wb = openpyxl.load_workbook(self.xlsx_address)
        self.ws = self.wb[self.sheet_name]

    def visit_poi_id(self, row_num):
        return self.ws[f'{self.poi_id_column}{row_num}'].value

    def visit_poi_name(self, row_num):
        return self.ws[f'{self.poi_name_column}{row_num}'].value

# 访问参考围栏, 如参考围栏为None, 访问参考位置
    def visit_reference_point_or_fence(self, row_num):
        fence_value = self.ws[f'{self.reference_fence_column}{row_num}'].value
        if fence_value == r'\N':
            return fence_value
        else:
            return self.ws[f'{self.reference_point_column}{row_num}'].value

# 写入'正确围栏'数据
    def write_correct_reference(self, row_num, correct_reference_data):
        self.ws[f'{self.correct_fence_column}{row_num}'] = correct_reference_data
        self.wb.save(self.xlsx_address)


# 画图工具
def draw_pic(reference_fence):
    # 2/ tool地址栏清空内容
    input_ele.fill('')
    # 3/ 输入'参考围栏'
    input_ele.fill(reference_fence)
    # 4/ 点击' draw it'
    draw_it_ele.click()
    # 5/ 点击'鼠标绘制面'
    mouse_draw_plane_ele.click()
    # 6/ 等待用户绘制图像
    page.locator('xpath=//*[@id="iCenter"]/div[1]/div/div[1]/div/div/div/div').wait_for(timeout=1000000, state='visible')
    # 7/ 获取 用户绘制图像产生的数据
    input_content = page.eval_on_selector('xpath=//*[@id="wkt"]', "(element) => element.value")
    return input_content


a = OperateXlsx()
row_num_1 = int(input('起始数:\n'))

with sync_playwright() as p:
    # 创建一个浏览器实例
    browser = p.chromium.launch(headless=False)
    # 创建含登录状态的浏览器上下文
    with open("baidu_state.json") as f:
        storage_state = json.loads(f.read())
    context1 = browser.new_context(storage_state=storage_state)
    context = browser.new_context(viewport={'width': 1536, 'height': 864})

    # 创建一个page对象
    page = context.new_page()
    while True:
        try:
            # 转到页面
            page.goto('https://page.cainiao.com/cntms/cnlbs/cnlbs_visual/cnlbs_visual.html')

            input_ele = page.locator('xpath=//*[@id="wkt"]')
            draw_it_ele = page.locator('xpath=//*[@id="draw"]')
            mouse_draw_plane_ele = page.locator('xpath=// *[ @ id = "polygon"]')

            input_information = a.visit_reference_point_or_fence(row_num_1)  # 1/ 从表格中获取参考围栏信息
            show_poi_name = a.visit_poi_name(row_num_1)  # 1.1/ 显示poi_name
            print(f'{row_num_1}, {show_poi_name}')
            # 2/ 在画图工具中产生输出信息----------------------------------
            output_information = draw_pic(input_information)
            a.write_correct_reference(row_num_1, output_information)  # 3/ 把输出信息写入到表格中
            row_num_1 += 1
        except:
            row_num_1 += 1
            # 创建一个page对象
            page = context.new_page()
