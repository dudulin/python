from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import cmd
import os

os.system("chcp 65001")


# 有权限问题 操作不了
# os.system(
#     r'cd C:\Program Files (x86)\Google\Chrome\Application && chrome.exe --remote-debugging-port=9222 --user-data-dir=“D:\auto”')


# 常用的行为有：
# 禁止图片和视频的加载：提升网页加载速度。
# 添加代理：用于翻墙访问某些页面，或者应对IP访问频率限制的反爬技术。
# 使用移动头：访问移动端的站点，一般这种站点的反爬技术比较薄弱。
# 添加扩展：像正常使用浏览器一样的功能。
# 设置编码：应对中文站，防止乱码。
# 阻止JavaScript执行。
# ————————————————
# cmd=> cd C:\Program Files (x86)\Google\Chrome\Application
# cmd=>chrome.exe --remote-debugging-port=9222 --user-data-dir=“D:\auto”
# 到浏览器 路径下的文件， 如果自动运行 之后运行 python


def create_dirver(config):
    if config['key'] == 'chrome':
        # 浏览器 通用配置
        # https://sites.google.com/a/chromium.org/chromedriver/capabilities 配置网站
        options = webdriver.ChromeOptions()

        # options.add_argument('--incognito')  # 隐身模式（无痕模式）

        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # 调用原来的浏览器，不用再次登录即可重启
        options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
        options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        chrome_driver = Chrome(options=options)
        return chrome_driver


driver = create_dirver({"key": "chrome"})
action = ActionChains(driver)  # 绑定事件对象

driver.get('https://www.1kkk.com/manhua-jp/')  # 打开网页
time.sleep(5)
# driver.maximize_window()

executor_url = driver.command_executor._url
session_id = driver.session_id

print(session_id)
print(executor_url)

time.sleep(10)

driver.quit()  # 退出关闭
