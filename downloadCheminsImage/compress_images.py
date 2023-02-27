# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/27 14:33
# File : compress_images.py
import os
from PIL import Image

# 压缩后的图片质量（0-100），值越低压缩后的图片越小但质量越差
COMPRESS_QUALITY = 50

# 图片文件格式列表，这里只列出了JPEG和PNG格式
IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']

# 遍历文件夹及子文件夹中的所有图片文件，并进行压缩
def compress_images(root_folder, output_folder):
    for root, dirs, files in os.walk(root_folder):
        # 构建输出目录
        output_root = root.replace(root_folder, output_folder)
        os.makedirs(output_root, exist_ok=True)

        for filename in files:
            if filename.lower().endswith(tuple(IMAGE_EXTENSIONS)):
                filepath = os.path.join(root, filename)
                # 构建输出文件路径
                output_path = os.path.join(output_root, filename)
                with Image.open(filepath) as img:
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    img.save(output_path, optimize=True, quality=COMPRESS_QUALITY)

# 调用compress_images函数压缩指定的文件夹中的所有图片文件
compress_images('G:\proprocess\downloadCheminsImage\传感器图片', 'G:\proprocess\downloadCheminsImage\压缩后传感器图片')
