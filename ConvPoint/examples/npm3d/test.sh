#!/usr/bin/env bash
python npm3d_seg.py --rootdir ./npm_processed --savedir ./results03/SegBig_intensity --test --savepts ;
python npm3d_seg.py --rootdir ./npm_processed --savedir ./results03/SegBig_nocolor --test --savepts --nocolor ;
python npm3d_seg_fusion.py --rootdir ./npm_processed --savedir ./results03/Fusion_8192pts --model_rgb ./results03/SegBig_intensity --model_noc ./results03/SegBig_nocolor --test --savepts ;
