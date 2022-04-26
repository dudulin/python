from selenium import webdriver
import time
# Chrome浏览器
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime


def create_chrome_driver(flag):
    if flag == 'chrome':
        option = webdriver.ChromeOptions()
        # 第一步，使用chrome开发者模式
        option.add_experimental_option(
            'excludeSwitches', ['enable-automation'])

        # 第二步，禁用启用Blink运行时的功能
        option.add_argument("--disable-blink-features=AutomationControlled")

        option.add_experimental_option("detach", True)
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
        option = webdriver.FirefoxOptions()
        fire_driver = Firefox(options=option)
        fire_driver.implicitly_wait(5)
        with open('stealthFile/stealth.min.js') as f:
            js = f.read()
        fire_driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {
                "source": js})
        return fire_driver


driver = create_chrome_driver('chrome')
action = ActionChains(driver)
driver.get('https://taobao.com/')


def get_btn(xpath):
    btn = driver.find_element(By.XPATH, xpath)
    return btn


def move_dom(obj, tim):
    action.move_to_element(obj).perform()
    time.sleep(tim)


def click_dom(tim):
    action.click().perform()
    time.sleep(tim)


def get_time(hour=False, minute=False, second=False, microsecond=False):

    time_now = datetime.datetime.now()
    h = hour if hour else time_now.hour
    m = minute if minute else time_now.minute
    s = second if second else time_now.second
    mic = microsecond if microsecond else time_now.microsecond

    time_start = datetime.datetime(
        time_now.year,
        time_now.month,
        time_now.day,
        h,
        m,
        s,
        mic)

    time_difference = time_start - time_now
    time1 = time_difference.total_seconds()
    return time1


time.sleep(3.6)
driver.maximize_window()

# 找到登录按钮
login_btn = driver.find_element(
    By.XPATH, '//div[@class="site-nav-menu-hd"]/div[@class="site-nav-sign"]/a[1]')
time.sleep(3)
action.move_to_element(login_btn).perform()
time.sleep(1.3)
action.click().perform()
time.sleep(3)
# action.context_click().perform()

btn1 = driver.find_element(By.XPATH, '//div[@id="login"]/div/i[1]')
action.move_to_element(btn1).perform()
time.sleep(1)

action.click().perform()

driver.implicitly_wait(40)
try:
    btn2 = driver.find_element(
        By.XPATH, '//div[@class="member-column-4"]/a[1]')
except Exception as e:
    print(e)
    print(f'耗时：')

time.sleep(2)
shop_car_btn = driver.find_element(By.XPATH, '//li[@id="J_MiniCart"]/div/a')
action.move_to_element(shop_car_btn).perform()
time.sleep(2)
action.click().perform()
time.sleep(3)
action.move_to_element(
    driver.find_element(
        By.XPATH,
        '//div[@id="J_SelectAll1"]')).perform()
time.sleep(1.3)
click_dom(3)

btn_go = get_btn('//a[@id="J_Go"]')
move_dom(btn_go, 2.3)

# =========================

# =========================


start_time = time.time()
# 时间必须 修改
different_time = get_time(minute=16)
time.sleep(different_time)
end_time = time.time()
print(end_time - start_time, different_time, '时间差')
# click_dom(0)

driver.implicitly_wait(5)
try:
    # driver.find_element(By.XPATH, '//div/a[@class="go-btn"]').click()
    print(666666666666666666666)
    cds = time.time()
    print(cds - start_time, '最后耗时', datetime.datetime.now())
except Exception as e:
    print(e)


# driver.close()
