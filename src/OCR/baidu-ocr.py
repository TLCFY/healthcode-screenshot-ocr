from aip import AipOcr
import re
import os
from pandas import DataFrame
from tqdm import tqdm

"""付费资源，需要替换"""
APP_ID = 'Your APP_ID'
API_KEY = 'Your API_KEY'
SECRET_KEY = 'Your SECRET_KEY'
""""""

""""可能需要修改的部分"""
pictureDIR = './test'
""""""

#建立应用
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def getFileList(dir,Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir: 文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            getFileList(newDir, Filelist, ext)

    return Filelist

pictureList = getFileList(pictureDIR,[],'png')
ocrResult = []
""""""""

""""开始处理图片"""
for picture in tqdm(pictureList):
    ocrResultItem = {}
    picturePath = f'{pictureDIR}\\{os.path.basename(picture)}'
    img = get_file_content(picture)

    # 调用baidu-ocr进行检测
    ocrResultMsg = client.basicGeneral(img)['words_result']
    x = [str(list(i.values())[0]) for i in ocrResultMsg]
    x_str = ','.join(x).replace('（请尽快接种新冠疫苗）', '')
    # 获取姓名
    name = re.compile(r',?([\u4e00-\u9fa5]{2,4}),')
    name = name.findall(x_str)
    # 获取最新的检测时间
    rnaDetectTime = re.search(r',((.){12})检测,',x_str)
    rnaDetectTime = rnaDetectTime.groups()
    # 获取截屏时间
    time = re.compile(r',(2022-(.){5})').findall(x_str)
    num = len(time) - 1
    time = time[num][0]
    # 获取健康码类别
    codeColor = re.compile(r',湖南(.+?)外省').findall(x_str)
    codeColor = str(codeColor)
    # try:
    #     name.remove('场所码')
    # except:
    #     pass
    ocrResultItem['截屏时间'] = time
    ocrResultItem['姓名'] = name[0]
    ocrResultItem['最新核酸检测时间'] = rnaDetectTime[0]
    ocrResultItem['电子健康颜色'] = codeColor[2:4]
    ocrResultItem['文件名'] = picture
    ocrResult.append(ocrResultItem)
# print(ocrResult)

ocrResult = DataFrame(ocrResult).to_excel('./test/result.xls')
