import visvis as vv
import numpy as np
import Args
import cv2


def count_parameters(net):
    return sum(p.numel() for p in net.parameters() if p.requires_grad)


def show3D(vols):
    vols = [vols.transpose(1, 0, 2)]
    f = vv.clf()
    a = vv.gca()
    m = vv.MotionDataContainer(a)
    for vol in vols:
        t = vv.volshow(vol)
        t.parent = m
        t.colormap = vv.ColormapEditor
    a.daspect = 1, 1, -1
    a.xLabel = 'x'
    a.yLabel = 'y'
    a.zLabel = 'z'
    app = vv.use()
    app.Run()


def read3D(path):
    data = np.load(path)
    data = data.transpose(1, 0, 2)
    data = data.reshape((1, 288, 400, 400))
    x_sum = np.sum(data, 1)
    out = 255 * (x_sum - np.min(x_sum)) / (np.max(x_sum) - np.min(x_sum))
    # cv2.imwrite("y.png", out[0, :, :])
    return data
