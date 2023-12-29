import os
import leafmap
from samgeo import SamGeo, tms_to_geotiff, get_basemaps
from PIL import Image

from torchgeo.datasets import BigEarthNet
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

import os

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


dataset = BigEarthNet(root='./dataset/', bands='s2', download=True, checksum=True)
# dataloader = DataLoader(dataset, batch_size=1)
# print(len(dataloader))

# print(dataloader)

print(len(dataset))