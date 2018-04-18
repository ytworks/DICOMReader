#! /usr/bin/env python
# coding:utf-8
from __future__ import print_function
import pydicom as dicom
import numpy as np
import sys
import os


def dicom_to_np(mri_file_path):
    # Extracting data from the mri file
    plan = dicom.read_file(mri_file_path)
    image_2d = np.array(plan.pixel_array)
    phototype = plan.PhotometricInterpretation
    Bits = plan.WindowWidth
    if phototype == 'MONOCHROME1':
        image_2d = float(Bits - 1) - image_2d
    return np.array(image_2d), Bits




if __name__ == '__main__':
    DICOM_PATH = './000136.dcm'

    X, _ = dicom_to_np(mri_file_path = DICOM_PATH)
    print(X)
