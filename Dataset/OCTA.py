import os
import h5py, cv2, imageio
import numpy as np
from PIL import Image
from os.path import join
import sys

sys.path.append("..")
import Args


def get_path_list(data_root_path, img_path, label_path):
    res = []
    if label_path != None:
        tmp_list = [img_path, label_path]
        for i in range(len(tmp_list)):
            data_path = data_root_path + '/' + tmp_list[i]
            filename_list = os.listdir(data_path)
            filename_list.sort()
            res.append([join(data_path, j) for j in filename_list])
    else:
        data_path = data_root_path + '/' + img_path
        filename_list = os.listdir(data_path)
        filename_list.sort()
        res.append([join(data_path, j) for j in filename_list])
    return res


def write_path_list(name_list, save_path, file_name):
    if file_name == "train.txt":
        f = open(join(save_path, file_name), 'w')
        for i in range(len(name_list[0])):
            f.write(str(name_list[0][i]) + " " + str(name_list[1][i]) + '\n')
        f.close()
    else:
        f = open(join(save_path, file_name), 'w')
        for i in range(len(name_list[0])):
            f.write(str(name_list[0][i]) + " " + str(name_list[1][i]) + '\n')
        f.close()


def Load(data_type):
    data_root_path = Args.Dataset
    img_train = "Data/" + data_type + "/Train/"
    gt_train = "GroundTruth/GroundTruth"
    img_valid = "Data/" + data_type + "/Validation/"
    gt_valid =  "GroundTruth/ValidTruth"
    save_path = "./content"
    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    train_list = get_path_list(data_root_path, img_train, gt_train)
    valid_list = get_path_list(data_root_path, img_valid, gt_valid)
    print('Number of train imgs:', len(train_list[0]))
    write_path_list(train_list, save_path, 'train_'+data_type+'.txt')
    print('Number of valid imgs:', len(valid_list[0]))
    write_path_list(valid_list, save_path, 'valid_'+data_type+'.txt')
    print("Finish!")


if __name__ == "__main__":
    Load("2D")
    Load("3D")
