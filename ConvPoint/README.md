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