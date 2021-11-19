import numpy as np
import cv2 as cv

# 画像データを入れる numpy.ndarray オブジェクト
image = np.zeros((256, 256, 3), np.uint8)

# テキストを描画する
text = "Hello, world"
org = (0, 100)
font_face = cv.FONT_HERSHEY_SIMPLEX
font_scale = 1.0
color = (0, 255, 127) # Blue, Green, Red
thickness = 1
line_type = cv.LINE_8
cv.putText(image, text, org, font_face, font_scale, color, thickness, line_type)

# 画像を出力する
path = "hello-world.png"
cv.imwrite(path, image)