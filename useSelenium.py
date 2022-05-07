from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time


#    写法过时  executable_path 不适用
# wb = webdriver.Chrome(executable_path=r'chromedriver/chromedriver.exe')
# s = Service(r'chromedriver/chromedriver.exe')  # 驱动器路径
wb = webdriver.Chrome()  # 配置
wb.maximize_window()
wb.get('https://www.baidu.com')
a = ActionChains(wb)

# 通过id 获取查询按钮
searchBtn = wb.find_element(By.ID, 'su')

# 通过id 获取输入框
searchInput = wb.find_element(By.ID, 'kw')

# 输入框 设置内容
searchInput.send_keys('输入的内容')

# 打印查询按钮的 value属性内容
print(searchBtn.get_attribute('value'),
      '打印查询按钮的 value属性内容====================')

a.drag_and_drop(searchInput, searchBtn).perform()

time.sleep(5)
searchBtn.send_keys(Keys.CONTROL, 'c')  # 复制

searchInput.send_keys(Keys.CONTROL, 'v')  # 粘贴


searchBtn.send_keys(Keys.ENTER)

# a.click(on_element=None)

# 由selenium的ActionChains类来完成模拟鼠标操作
# 主要操作流程:
# 1.存储鼠标操作
# 2.perform()来执行鼠标操作
time.sleep(3)  # 因为异步
# 移动到 输入框
a.move_to_element(wb.find_element(By.ID, 'kw')).perform()
time.sleep(3)
# 存储鼠标操作 右键单击
a.context_click(on_element=None)
# 存储鼠标操作 左键单击
# a.click(on_element=None)
# 执行鼠标操作
a.perform()

# 支持的操作如下:
# double_click()  双击操作
# context_click()  右击操作
# drag_and_drop()  拖拽操作.左键按住拖动某一个元素到另一个区域,然后释放按键
# move_to_element()  鼠标悬停,常会用到


# searchInput = wb.find_element(By.XPATH, '//div[@id="u1"]//a[@name="tj_settingicon"]')
# print(searchInput.get_attribute('name'), 'searchInput.name====================')


time.sleep(5)

wb.close()
