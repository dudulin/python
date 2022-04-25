from selenium import webdriver


wb = webdriver.Chrome(executable_path=r'chromedriver/chromedriver.exe')  # 获取谷歌浏览器驱动
wb.get('https://www.baidu.com')