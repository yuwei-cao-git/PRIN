# ConvPoint for urban environment classification 

## Platform

The code was tested on Ubuntu 22.04 with Miniconda.

## Dependencies

- Pytorch
- Scikit-learn for confusion matrix computation, and efficient neighbors search  
- TQDM for progress bars
- PlyFile
- H5py

All these dependencies can be install via conda in an Anaconda environment or via pip.

## Installation:
1. Following this link install cuda-toolkit and cudnn: https://gist.github.com/amir-saniyan/b3d8e06145a8569c0d0e030af6d60bea

2. Install Development Tools
```
    $ sudo apt install build-essential pkg-config cmake cmake-qt-gui ninja-build valgrind
```
3. Install Python 3
```
    $ sudo apt install python3 python3-wheel python3-pip python3-venv python3-dev python3-setuptools
```
4. Install miniconda:
```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh

$ ./Miniconda3-latest-Linux-x86_64.sh

$ source ~/miniconda3/bin/activate 
$ conda config --set auto_activate_base true
$ conda deactivate
```
5. Install pytorch'gpu:
```
conda create --name torchgpu python=3.6
conda activate torchgpu

pip install --upgrade pip setuptools wheel
pip install --upgrade opencv-python opencv-contrib-python
pip install --upgrade torch torchvision torchaudion
```
6. install dependencies:
```
pip install -r requirements.txt
```

## Compile the libraries

### Nearest neighbor module

The ```nearest_neighbors``` directory contains a very small wrapper for [NanoFLANN](https://github.com/jlblancoc/nanoflann) with OpenMP.
To compile the module:
```
cd nearest_neighbors
python setup.py install --home="."
```
## Model training and Testing

### Model 1: MNMPNPM3d_Sigbig_nocolor

#### Data preparation

```
python npm3d_prepare_data.py --rootdir ./data --destdir ./data/npm_processed

```

#### Training

```
python npm3d_seg.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor/results --nocolor

```
#### Testing

```
python mantua_seg_test.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor_Mapped_NPM/ --nocolor --test --savepts

```
#### Generate Test Result

```
python mantua_full_cloud_gen.py 

```

---

### Model 2: Fine-tuning pretrained npm_sigbig_nocolor model: MNPM_pretrained_npm3d_Sigbig_nocolor

```
python npm3d_seg.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor/results --nocolor --restore
```
#### Testing
```
python npm3d_seg.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor_pretrained_mnmp/SegBig_8192_nocolor_FT --nocolor --restore --test --savepts
``` 
-----------

### Model 3: MNPM_Semantic3d_Sigbig_nocolor

#### Data preparation
```
cd examples/semantic3d/

prepare semantic format data and labels:

```
cd data
python
import numpy as np
import pandas as pd

pc = np.loadtxt(orignialpc_filename) 
# pc=np.loadtxt("./data/mantua_labelled_wp1.txt")
label = pc[..., -1].astype(np.uint8)
label_df=pd.DataFrame(label)
label_df.to_csv(filename, index=False)
# label_df.to_csv("./data/mantua_labelled_wp1.labels", index=False)
```

python semantic3d_prepare_data.py --rootdir ./data
```
#### Training
```
python semantic3d_seg.py --rootdir ./semantic3d_processed/train/pointcloud --savedir ./results/SegBig_nocolor_nmp/ --nocolor
```
#### Testing
```
python semantic3d_seg.py --rootdir ./semantic3d_processed/test/pointcloud --savedir ./results/SegBig_nocolor_nmp/SegBig_8192_nocolor --nocolor --test --savepts
```
--------------------
### Model 4: Fine-tuning pretrained semantic3d_sigbig_nocolor model: MNPM_pretrained_Semantic3d_Sigbig_nocolor

```
python semantic3d_seg.py --rootdir ./semantic3d_processed/train/pointcloud --savedir ./results/SegBig_nocolor_nmp/ --nocolor --restore
```
#### Testing
```
python semantic3d_seg.py --rootdir ./semantic3d_processed/test/pointcloud --savedir ./results/SegBig_nocolor_nmp/SegBig_8192_nocolor_FT --nocolor --restore --test --savepts
``` 
-----------
