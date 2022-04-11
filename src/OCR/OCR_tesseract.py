from PIL import Image
import pytesseract

# 调用tesseract识别图像，返回图像中的简体中文和数字
def imageOCR(imageInputPath):
    text = pytesseract.image_to_string(Image.open(imageInputPath), lang='chi_sim')
    return text