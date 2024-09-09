import os
import shutil

# 设置JPEGImages和txt文件夹的路径
jpeg_images_path = r'C:\Users\mine\Desktop\server\RT-DETR\RTDETR-main\dataset\VOCdevkit\JPEGImages'
txt_path = r'C:\Users\mine\Desktop\server\RT-DETR\RTDETR-main\dataset\VOCdevkit\txt'
folder_a_path = r'C:\Users\mine\Desktop\server\RT-DETR\RTDETR-main\dataset\VOCdevkit\txtlabel'
folder_b_path = r'C:\Users\mine\Desktop\server\RT-DETR\RTDETR-main\dataset\VOCdevkit\nolable_img'

# 创建文件夹A和B，如果它们不存在的话
os.makedirs(folder_a_path, exist_ok=True)
os.makedirs(folder_b_path, exist_ok=True)

# 遍历JPEGImages文件夹中的每个图像文件
for image_name in os.listdir(jpeg_images_path):
    # 去除图像文件名的扩展名
    base_name = os.path.splitext(image_name)[0]
    # 对应的txt文件的路径
    txt_file_name = base_name + '.txt'
    txt_file_path = os.path.join(txt_path, txt_file_name)

    # 检查对应的txt标签文件是否存在
    if os.path.isfile(txt_file_path):
        # 如果对应的txt文件存在，将它复制到文件夹A
        shutil.copy2(txt_file_path, os.path.join(folder_a_path, txt_file_name))
    else:
        # 如果txt文件不存在，删除JPEGImages文件夹中的图片
        os.remove(os.path.join(jpeg_images_path, image_name))

# 这段代码将完成您的要求，但请记得将路径替换成您的实际文件夹路径。

