from selenium import webdriver
from selenium.webdriver import Chrome


# 统一的 浏览器配置

def create_driver(flag):
    if flag == 'chrome':
        option = webdriver.ChromeOptions()
        # ==============================================

        # ==============================================

        # 第一步，使用chrome开发者模式
        # option.add_experimental_option(
        #     'excludeSwitches', ['enable-automation'])
        #
        # # 第二步，禁用启用Blink运行时的功能
        # option.add_argument("--disable-blink-features=AutomationControlled")
        # option.add_argument("–incognito")
        # prefs = {"profile.managed_default_content_settings.images": 2
        #          }

        # option.add_experimental_option("prefs", prefs)

        # option.add_experimental_option(
        #     'excludeSwitches',
        #     ['enable-automation'])  # 模拟真正浏览器
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        # option.add_experimental_option("detach", True)
        # 无头浏览器需要添加user-agent来隐藏特征
        option.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36')
        chrome_driver = Chrome(options=option)
        chrome_driver.implicitly_wait(5)
        with open('stealthFile/stealth.min.js') as f:
            js = f.read()
        chrome_driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {
                "source": js})
        chrome_driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                            Object.defineProperty(navigator, 'webdriver', {
                              get: () => undefined
                            })
                          """})

        return chrome_driver
    else:
        print(flag)
# option = webdriver.FirefoxOptions()
# fire_driver = Firefox(options=option)
# fire_driver.implicitly_wait(5)
# with open('stealthFile/stealth.min.js') as f:
#     js = f.read()
# fire_driver.execute_cdp_cmd(
#     "Page.addScriptToEvaluateOnNewDocument", {
#         "source": js})
# return fire_driver
