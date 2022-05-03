# HealthCode-Screenshot-OCR

识别并统计健康码截图中的个人信息

## Collaborator

- [@TLCFY](https://github.com/TLCFY/)

## Dev Log

- **2022-5-3：**

  构造了对本地图片处理的可用脚本

  接下来将尝试自动提取微信图片

- **2022-5-2：**

  利用本地文件尝试调用了`baidu-ocr SDK`，识别准确率良好

  输出结果格式化为`result.xls`文件

- **2022-4-13：**

  `OCR_baidu.py`报错：`ModuleNotFoundError: No module named 'chardet'`，执行命令`pip install chardet`解决。

- **2022-4-12：**

  建立新的工作分支`baidu-ocr`

  暂停`main`分支中根据`pytesseract-ocr`搭建`OCR`引擎工作
  
  获取`baidu-aip`调用接口

  申请百度`OCR`免费测试资源

## Package-Installation

1. 安装百度官方`OCR`依赖包`baidu-aip`、`chardet`

    ```shell
    pip install baidu-aip
    pip install chardet
    ```
    
2. 根据提示安装其他依赖包

