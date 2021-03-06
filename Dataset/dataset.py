# 子控制文件，负责将指定文件地址的数据集转换为可训练形式
import sys

sys.path.append("..")
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import numpy as np


def default_loader(path):
    return Image.open(path)


def numpy_loader(path):
    return np.load(path)


class MyDataset(Dataset):
    def __init__(self, txt, transform=None, target_transform=None, loader=default_loader, target_loader=default_loader):
        super(MyDataset, self).__init__()
        fh = open(txt, 'r')
        imgs = []
        for line in fh:
            line = line.strip('\n')
            line = line.rstrip('\n')
            words = line.split()
            imgs.append((words[0], words[1]))
        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform
        self.loader = loader
        self.target_loader = target_loader

    def __getitem__(self, index):
        fn, label = self.imgs[index]
        img = np.array(self.loader(fn), dtype=float)
        target = np.array(self.target_loader(label), dtype=float)
        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            target = self.target_transform(target)
        return img, target

    def __len__(self):
        return len(self.imgs)
