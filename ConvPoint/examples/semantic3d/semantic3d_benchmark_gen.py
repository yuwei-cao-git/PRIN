import numpy as np
import semantic3D_utils.lib.python.semantic3D as sem3D
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--testdir', '-s', help='Path to data folder')
parser.add_argument("--savedir", type=str, default="./results")
parser.add_argument("--refdata", type=str, default="./results")
parser.add_argument("--reflabel", type=str, default="./results")
args = parser.parse_args()

filenames = [
        ["mantua_x120_2_xyzrgb", "mantua_x120_2_xyzrgb_benchmark.label"],
        ["mantua_x120_1_xyzrgb", "mantua_x120_1_xyzrgb_benchmark.label"],
]

os.makedirs(args.savedir, exist_ok=True)

for fname in filenames:
    print(fname[0])
    data_filename = os.path.join(args.testdir, fname[0]+".txt")
    dest_filaname = os.path.join(args.savedir, fname[1])
    refdata_filename = os.path.join(args.refdata, fname[0]+"_voxels.txt")
    reflabel_filename = os.path.join(args.reflabel, fname[0]+"_voxels.npy")

    sem3D.project_labels_to_pc(dest_filaname, data_filename, refdata_filename, reflabel_filename)
