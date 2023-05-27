'''
input: 3x   64x64
conv1: 64x  32x32
conv2: 128x 16x16
conv3: 256x 8x8
conv4: 512x 4x4
avgpool: 512x 1x1
fc: 1000
'''

'''
creat a new val similar to train
'''
import os
import shutil

data_dir = "D:/mycode/code/python_program/tiny-imagenet-200"
val_dir = os.path.join(data_dir , "val")
val_image_dir = os.path.join(val_dir, "images")
annotations_path = os.path.join(val_dir,"val_annotations.txt")
wnids_path = os.path.join(data_dir, "wnids.txt")
val_new = os.path.join(data_dir, "val_new")
os.mkdir(val_new)

with open(annotations_path,"r") as an:
    lines_an = an.readlines()

    with open(wnids_path,"r") as wnids:
        lines_wnids = wnids.readlines()

        for an_num, line_an in enumerate(lines_an):
            line_an_fine = line_an.split("\t")
            img_name = line_an_fine[0]
            img_type = line_an_fine[1]

            for wnids_num, line_wnids in enumerate(lines_wnids):
                if(img_type == line_wnids.rstrip("\n")):
                    label = wnids_num
                    label_path = os.path.join(val_new,str(label))


                    if(not os.path.exists(label_path)):
                        os.mkdir(label_path)

                    image = os.path.join(val_image_dir,img_name)
                    shutil.copy(image,label_path)
