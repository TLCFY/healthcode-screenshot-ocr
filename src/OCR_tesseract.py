from PIL import Image

import pytesseract

# 测试数据地址
testDataAddr = './test/'
print(pytesseract.image_to_string(Image.open('./test/test-green.jpg'), lang='chi_sim'))