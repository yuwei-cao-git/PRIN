# Semantic Segmentation Example

## Data

Mapped NPM3D data can be found at [here](../../original_data/Mapped_NPM_Benchmark)

```
cd examples/semantic3d/
python
```
prepare data following semantic format data and labels:

```
import numpy as np
import pandas as pd

pc = np.loadtxt(orignialpc_filename) 
# pc = np.loadtxt("./data/mantua_labelled_wp1.txt")
label = pc[..., -1].astype(np.uint8)
label_df = pd.DataFrame(label)
label_df.to_csv(filename, index=False)
# label_df.to_csv("./data/mantua_labelled_wp1.labels", index=False)
```

For the training & test set:
```
python semantic3d_prepare_data.py --rootdir ./data
```

For only the test set: (use it when you want to test on another data)
```
python semantic3d_prepare_data_test.py --rootdir ./data
```

## Training
### use mapped npm3d dataset to train 
```
python semantic3d_seg.py --rootdir ./semantic3d_processed/train/pointcloud --savedir ./results/SegBig_nocolor_NPM/ --nocolor --dataset "MNPM"
```
### use mapped npm3d dataset + mantua_labelled_wp1 to train 
```
python semantic3d_seg.py --rootdir ./semantic3d_processed/train/pointcloud --savedir ./results/SegBig_nocolor_MMNPM/results --nocolor --dataset "MMNPM"
```
### use mapped npm3d dataset to train and then use mantua_labelled_wp1 to finetuning 
```
python semantic3d_seg.py --rootdir ./semantic3d_processed/train/pointcloud --savedir ./results/SegBig_nocolor_Mantua --nocolor --restore --epoch 15 --dataset "Mantua"
```

## Testing

```
python semantic3d_seg.py --rootdir ./semantic3d_processed/test/pointcloud --savedir ./results/SegBig_nocolor_NPM/ --nocolor --test --savepts
```

```
python semantic3d_seg.py --rootdir ./semantic3d_processed/test/pointcloud --savedir ./results/SegBig_nocolor_MMNPM/ --nocolor --test --savepts
```

```
python semantic3d_seg.py --rootdir ./semantic3d_processed/test/pointcloud --savedir ./results/SegBig_nocolor_Mantua/SegBig_8192_nocolor_pretrained_SN_FT --nocolo
r --test --savepts
```

```
## benchmark generation
```
python semantic3d_benchmark_gen.py --testdir ./data --savedir ./results/SegBig_nocolor/results --refdata ./semantic3d_processed/test/pointcloud_txt --reflabel ./results/SegBig_nocolor/results 
```
## project labels and voxels to pts
```
python semantic3d_full_cloud_gen.py
```

## Pretrained models
### train with npm:
Pretrained models can be found [here](https://github.com/aboulch/ConvPoint/releases/download/0.1.0/models_NPM3D_v0.zip).

### train with mapped npm:
Pretrained models can be found
### train with mapped npm + mantua_wp1:
Pretrained models can be found
### train with mapped npm then finetuned with mantua_wp1:
Pretrained models can be found