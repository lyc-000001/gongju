import cv2
import numpy as np


def detect(src_img, dst_img):
    # 确保两张图像尺寸相同
    if src_img.shape != dst_img.shape:
        dst_img = cv2.resize(dst_img, (src_img.shape[1], src_img.shape[0]))
    # 对原始图像和目标图像进行高斯模糊，以减少噪声影响
    src_img = cv2.GaussianBlur(src_img, [5, 5], 0)
    dst_img = cv2.GaussianBlur(dst_img, [5, 5], 0)

    # 计算两张图像的差异
    diff = cv2.absdiff(src_img, dst_img)

    # 转换为灰度图
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # 应用阈值化，得到二值图像
    _, result = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

    # 对二值图像进行膨胀，突出差异区域
    result = cv2.dilate(result, np.ones([5, 5]))

    # 寻找差异区域的轮廓
    contours, _ = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = []

    # 计算轮廓面积
    for c in contours:
        area = cv2.contourArea(c)
        areas.append(area)
    areas = np.array(areas)
    index = np.argsort(areas)

    top_contours = [contours[i] for i in index]
    rect_pos = [cv2.boundingRect(c) for c in top_contours]

    return rect_pos


# 读取原始图像和目标图像
src_img = cv2.imread("test-2.jpg")
dst_img = cv2.imread("test-5.jpg")

# 调用差异检测函数，获取差异区域的矩形坐标
rects = detect(src_img, dst_img)

# 在目标图像上标注差异区域
for x, y, w, h in rects:
    cv2.rectangle(dst_img, [x, y], [x + w, y + h], [0, 0, 255], 3)

# 显示原始图像和标注差异的目标图像
cv2.imshow("test-2.jpg", src_img)
cv2.imshow("test-5.jpg", dst_img)
cv2.waitKey(0)
