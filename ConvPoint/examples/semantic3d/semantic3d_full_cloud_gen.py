import numpy as np
from os.path import join, dirname
import pandas as pd
from helper_ply import write_ply

def load_pc_semantic3d(filename):
    pc = np.loadtxt(filename)
    return pc

def load_label_semantic3d(filename):
    label_pd = pd.read_csv(filename, header=None, delim_whitespace=True, dtype=np.uint8)
    cloud_labels = label_pd.values
    return cloud_labels

pc_paths = [
		'./data/stonex_tutte.txt',
]

for pc_path in pc_paths:
	pc = load_pc_semantic3d(pc_path)
	file_name = pc_path.split('/')[-1][:-4]

	# check if label exists
	label_path = join('./results/SegBig_nocolor_Mantua/SegBig_8192_nocolor_MMNPM/results', file_name + '_benchmark.label')
	labels = load_label_semantic3d(label_path)

	full_ply_path = join(dirname(label_path), file_name + '_full_cloud.ply')

	write_ply(full_ply_path, [pc, labels], ['x', 'y', 'z', 'intensity', 'red', 'green', 'blue', 'class'])
