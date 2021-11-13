from cv2 import cv2
import numpy as np
import os




def listdir(path, list):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list)
        elif os.path.splitext(file_path)[1] == '.jpg':
            list.append(file_path)

def cut():
    for i in range(len(list)):
        input_img = list[i]
        # pic_path = '.jpg'  # 分割的图片的位置
        pic_target = 'cut_result/img%s_'%(i+1)  # 分割后的图片保存的文件夹
        # 要分割后的尺
        cut_width = 416
        cut_length = 416
        # 读取要分割的图片，以及其尺寸等数据
        picture = cv2.imread(input_img)
        (width, length, depth) = picture.shape
        # 预处理生成0矩阵
        pic = np.zeros((cut_width, cut_length, depth))
        # 计算可以划分的横纵的个数
        num_width = int(width / cut_width)
        num_length = int(length / cut_length)

        # for循环迭代生成
        for k in range(0, num_width):
            for j in range(0, num_length):
                pic = picture[k * cut_width: (k + 1) * cut_width, j * cut_length: (j + 1) * cut_length, :]
                result_path = pic_target+'{}_{}.jpg'.format(k + 1, j + 1)
                cv2.imwrite(result_path, pic)
                with open("img/cut_images_name.txt", "a") as file:
                    file.write('{}_{}'.format(k + 1, j + 1) + "\n")

        print("第%s张分割完成!" % (i + 1))


path=r'C:\Users\Admin\PycharmProjects\cut\img\test'
list=[]
listdir(path,list)

cut();


