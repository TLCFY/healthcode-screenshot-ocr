from aip import AipOcr
import os

"""付费资源，需要替换"""
APP_ID = '25953512'
API_KEY = 'tGROK4KObFUoE2UFLm7PvfNT'
SECRET_KEY = 'tYkFiGmp9XQl3UO20zqafGvn7HSOh8zU'
""""""

#建立应用
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
