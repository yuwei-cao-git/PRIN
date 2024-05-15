import numpy as np
from os.path import join, dirname
import pandas as pd
from helper_ply import write_ply
from plyfile import PlyData
import argparse

def load_pc_mantua(filename):
    plydata=PlyData.read(filename)
    x = plydata["vertex"].data["x"].astype(np.float32)
    y = plydata["vertex"].data["y"].astype(np.float32)
    z = plydata["vertex"].data["z"].astype(np.float32)
    r = plydata["vertex"].data["red"].astype(np.int8)
    g = plydata["vertex"].data["green"].astype(np.int8)
    b = plydata["vertex"].data["blue"].astype(np.int8)
    reflectance = plydata["vertex"].data["scalar_Intensity"].astype(np.float32)
    pts = np.concatenate([
                np.expand_dims(x,1).astype(np.float32),
                np.expand_dims(y,1).astype(np.float32),
                np.expand_dims(z,1).astype(np.float32),
                np.expand_dims(r,1).astype(np.int8),
                np.expand_dims(g,1).astype(np.int8),
                np.expand_dims(b,1).astype(np.int8),
                np.expand_dims(reflectance,1).astype(np.float32),
                ], axis=1)
    return pts

def load_label_mantua(filename):
    labels = np.loadtxt(filename)
    cloud_labels = np.expand_dims(labels,1).astype(np.int8)
    return cloud_labels


parser = argparse.ArgumentParser()
parser.add_argument('--pc_path', '-s', help='Path to data', default='./data/test_original/stonex_partial.ply')
parser.add_argument("--label_path", type=str, default="./results")
args = parser.parse_args()

pc_path = args.pc_path
pc = load_pc_mantua(pc_path)
file_name = pc_path.split('/')[-1][:-4]

# check if label exists
label_path = args.label_path
labels = load_label_mantua(label_path)

full_ply_path = join(dirname(label_path), file_name + '_predt_cloud.ply')

write_ply(full_ply_path, [pc, labels], ['x', 'y', 'z', 'red', 'green', 'blue', 'intensity', 'class'])
