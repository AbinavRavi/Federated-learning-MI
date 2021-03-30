import nibabel as nib
import numpy as np
from glob import glob

def to_slice(image_path,seg_path):
    image = nib.load(image_path).get_fdata()
    seg = nib.load(seg_path).get_fdata()
    image_list = []
    seg_list = []
    for i in range(image.shape[2]):
        if(np.nonzero(image[i])!= 0):
            image_list.append(image[i])
            seg_list.append(seg[i])
    return image_list,seg_list



