# 平均值法进行图像灰度化
import cv2
from OCR import OCR_tesseract


def gray_mean_rgb(inputimagepath,outimagepath):
    img = cv2.imread(inputimagepath)
    gray_mean_rgb_image = img.copy()
    img_shape = img.shape
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            gray_mean_rgb_image[i,j] = (int(img[i,j][0])+int(img[i,j][1])+int(img[i,j][2]))/3
    cv2.imwrite(outimagepath, gray_mean_rgb_image)  # 保存当前灰度值处理过后的文件

inputimagepath = "./test/test-green.jpg"
outimagepath = "./test/test-green-gmrgb.jpg"
gray_mean_rgb(inputimagepath,outimagepath)

print(OCR_tesseract.imageOCR(outimagepath))