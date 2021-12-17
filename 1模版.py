# git 同步
# excel 生成函数
import pandas as pd
import numpy as np
from fake_user_agent.main import user_agent


def createExcel():
    data = np.arange(1, 101).reshape((10, 10))
    print(data)
    data_df = pd.DataFrame(data)
    data_df.columns = ['11', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    data_df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    writer = pd.ExcelWriter('my.xlsx')
    data_df.to_excel(writer, float_format='%.5f')
    writer.save()


def getUserAgent():
    dd = user_agent('chrome')  # 浏览器版本模块
    return dd


ua = getUserAgent()
print(ua, 'ua33')
