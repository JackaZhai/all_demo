import os, shutil, random
from tqdm import tqdm

"""
标注文件是yolo格式（txt文件）
训练集：验证集：测试集 （7：2：1） 
"""


def split_img(img_path, label_path, split_list):
    try:
        Data = 'D:/TestMain/yolov9-main/datasets/fish/ImageSets'
        # Data是你要将要创建的文件夹路径（路径一定是相对于你当前的这个脚本而言的）
        # os.mkdir(Data)

        train_img_dir = Data + '/images/train'
        val_img_dir = Data + '/images/val'
        test_img_dir = Data + '/images/test'

        train_label_dir = Data + '/labels/train'
        val_label_dir = Data + '/labels/val'
        test_label_dir = Data + '/labels/test'

        # 创建文件夹
        os.makedirs(train_img_dir)
        os.makedirs(train_label_dir)
        os.makedirs(val_img_dir)
        os.makedirs(val_label_dir)
        os.makedirs(test_img_dir)
        os.makedirs(test_label_dir)

    except:
        print('文件目录已存在')

    train, val, test = split_list# 0.7, 0.2, 0.1
    all_img = os.listdir(img_path)# 获取所有图片的名字
    all_img_path = [os.path.join(img_path, img) for img in all_img]# 获取所有图片的路径
    # all_label = os.listdir(label_path)# 获取所有标注文件的名字
    # all_label_path = [os.path.join(label_path, label) for label in all_label]# 获取所有标注文件的路径
    train_img = random.sample(all_img_path, int(train * len(all_img_path)))# 随机选取70%的图片作为训练集
    train_img_copy = [os.path.join(train_img_dir, img.split('\\')[-1]) for img in train_img]# 将训练集的图片复制到指定文件夹
    train_label = [toLabelPath(img, label_path) for img in train_img]# 获取训练集的标注文件
    train_label_copy = [os.path.join(train_label_dir, label.split('\\')[-1]) for label in train_label]# 将训练集的标注文件复制到指定文件夹
    for i in tqdm(range(len(train_img)), desc='train ', ncols=80, unit='img'):# tqdm是一个进度条库
        _copy(train_img[i], train_img_dir)# 复制训练集的图片
        _copy(train_label[i], train_label_dir)#复制训练集的标注文件
        all_img_path.remove(train_img[i])# 删除已经复制的图片
    val_img = random.sample(all_img_path, int(val / (val + test) * len(all_img_path)))
    val_label = [toLabelPath(img, label_path) for img in val_img]
    for i in tqdm(range(len(val_img)), desc='val ', ncols=80, unit='img'):
        _copy(val_img[i], val_img_dir)
        _copy(val_label[i], val_label_dir)
        all_img_path.remove(val_img[i])
    test_img = all_img_path
    test_label = [toLabelPath(img, label_path) for img in test_img]
    for i in tqdm(range(len(test_img)), desc='test ', ncols=80, unit='img'):
        _copy(test_img[i], test_img_dir)
        _copy(test_label[i], test_label_dir)


def _copy(from_path, to_path):
    shutil.copy(from_path, to_path)


def toLabelPath(img_path, label_path):
    img = img_path.split('\\')[-1]
    label = img.split('.jpg')[0] + '.txt'
    return os.path.join(label_path, label)


if __name__ == '__main__':
    img_path = 'D:\TestMain\yolov9-main\datasets\\fish\images'  # 你的图片存放的路径（路径一定是相对于你当前的这个脚本文件而言的）
    label_path = 'D:\TestMain\yolov9-main\datasets\\fish\lables'  # 你的txt文件存放的路径（路径一定是相对于你当前的这个脚本文件而言的）
    split_list = [0.8, 0.18, 0.02]  # 数据集划分比例[train:val:test]
    split_img(img_path, label_path, split_list)
