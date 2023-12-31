import os
import leafmap
from samgeo import SamGeo, tms_to_geotiff, get_basemaps
from PIL import Image
from typing import Callable, Optional
from torch import Tensor

from torchgeo.datasets import BigEarthNet
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

import os

# reference
# https://pytorch.org/blog/geospatial-deep-learning-with-torchgeo/

# use when download torchgeo dataset
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def leafe_map():
    m = leafmap.Map(center=[29.676840, -95.369222], zoom=19)
    m.add_basemap("SATELLITE")
    # m.save("my_map.html")

    # image = "satellite.tif"
# leafe_map()

def read_tif():
    tiff_image = Image.open("tif/S2A_MSIL2A_20170613T101031_0_45_B01.tif")
    tiff_image = Image.open("satellite.tif")
    jpeg_image = tiff_image.convert("RGB")
    jpeg_image.show()
    print(jpeg_image)
# read_tif()
        

dataset = BigEarthNet(root='./BigEarthNet/', bands='s2', download=False, checksum=False)


print('type: ', type(dataset[0]))
print('keys: ', dataset[0].keys())
print('label size', dataset[0]['label'].size())
# print(dataset.folders[0]) # path
# print(dataset.class_sets[19]) # label names
print('image size: ', dataset[0]['image'].size())

# get label names
label_mask = dataset[0]['label']
label_name = dataset._onehot_labels_to_names(label_mask)
print('label name: ', label_name, '\n')

# dataloader
dataloader = DataLoader(dataset, batch_size=1)
for batch in dataloader:
    print(batch['image'].size())
    print(batch['label'])
    break

# plot dataset image
fig = dataset.plot(dataset[0])
plt.show()