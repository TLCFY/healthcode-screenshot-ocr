from PIL import Image
import pytesseract
import sys

# 测试数据地址
testDataAddr = sys.argv[1]
print(pytesseract.image_to_string(Image.open(testDataAddr), lang='chi_sim'))
