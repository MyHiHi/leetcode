

# coding: utf8
import cv2 as cv
import os
import time
# 替换字符列表
ascii_char = list(
    r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
print(len(ascii_char))
# char_len = len(ascii_char)
# # 加载视频
# cap = cv.VideoCapture('D:\\1.mp4')
# while True:
#     # 读取视频每一帧
#     hasFrame, frame = cap.read()
#     if not hasFrame:
#         break
#     # 视频长宽
#     width = frame.shape[0]
#     height = frame.shape[1]
#     # 转灰度图
#     img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # 缩小图片并调整长宽比
#     img_resize = cv.resize(img_gray, (int(width / 10), int(height / 10)))

#     text = ''
#     # 遍历图片中的像素
#     for row in img_resize:
#         for pixel in row:
#             # 根据像素值，选取对应的字符
#             text += ascii_char[int(pixel / 256 * char_len)]
#         text += '\n'
#     # 清屏
#     os.system('cls')  # mac是'clear'
#     # 输出生成的字符方阵
#     print(text)
#     # 适当暂停一下
#     time.sleep(0.98)
