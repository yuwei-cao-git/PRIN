data prepare:
python semantic3d_prepare_data_test.py --rootdir ./data

inference:
python semantic3d_seg.py --rootdir ./semantic3d_processed/test/pointcloud --savedir ./results/SegBig_nocolor --test --savepts --nocolor

benchmark generation:
python semantic3d_benchmark_gen.py --testdir ./data --savedir ./results/SegBig_nocolor/results --refdata ./semantic3d_processed/test/pointcloud_txt --reflabel ./results/SegBig_nocolor/results 

project labels and voxels to ptcs
python semantic3d_full_cloud_gen.py
