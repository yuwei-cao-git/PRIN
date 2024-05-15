# NPM3D example

## Data

Original NPM3D Data can be downloaded at [http://npm3d.fr/paris-lille-3d](http://npm3d.fr/paris-lille-3d).

Mapped NPM3D data can be found at [here](../../original_data/Mapped_NPM_Benchmark)

The script ```npm3d_prepare_data.py``` can be used to split the point clouds and save them at numpy format.

For the training set:
```
python npm3d_prepare_data.py --rootdir ./data --destdir ./data/npm_processed
```

For the test set:
```
python npm3d_prepare_data.py --rootdir ./data --destdir ./data/npm_processed --test
```

## Training
### use mapped npm3d dataset to train 
```
python npm3d_seg.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor_NPM/results
```
### use mapped npm3d dataset + mantua_labelled_wp1 to train 
```
python npm3d_seg.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor_MMNPM/results --nocolor
```
### use mapped npm3d dataset to train and then use mantua_labelled_wp1 to finetuning 
```
python npm3d_seg.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor_pretrained_mnmp/results --nocolor --restore
```

## Testing

```
python mantua_seg_test.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor_NPM/ --nocolor --test --savepts
```

```
python mantua_seg_test.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor_MMNPM/ --nocolor --test --savepts
```

```
python npm3d_seg.py --rootdir ./data/npm_processed/ --savedir ./results/SegBig_nocolor_pretrained_mnmp/SegBig_8192_nocolor_FT --nocolor --test --savepts
```

**note**: the `test_step` parameter is set `0.8`. It is possible to change it. A smaller step of sliding window would produce better segmentation at a the cost of a longer computation time.

## Generate Test Result

```
python mantua_full_cloud_gen.py 

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