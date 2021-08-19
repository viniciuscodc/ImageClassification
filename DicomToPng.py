import pydicom as dicom
import os
import cv2

Categories=['non-lung','normal','emphysema','ground-glass','fibrosis','micronodules','consolidation']

# make it True if you want in PNG format
PNG = True

# Specify the .dcm folder path
folder_path_r = "ImagesLabeled"

# Specify the output jpg/png folder path
jpg_folder_path_r = "ImagesConvertedLabeled"
if not os.path.isdir(jpg_folder_path_r):
    os.mkdir(jpg_folder_path_r)

def convert():
    for i,category in enumerate(Categories):

        folder_path = os.path.join(folder_path_r,str(i))
        jpg_folder_path = os.path.join(jpg_folder_path_r,str(i))

        if not os.path.isdir(jpg_folder_path):
            os.mkdir(jpg_folder_path)
        
        images_path = os.listdir(folder_path)
        for n, image in enumerate(images_path):
            ds = dicom.dcmread(os.path.join(folder_path, image))
            pixel_array_numpy = ds.pixel_array
            if PNG == False:
                image = image.replace('.dcm', '.jpg')
            else:
                image = image.replace('.dcm', '.png')
            cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
            if n % 100 == 0:
                print('{} image converted'.format(n))

convert()
print('Done')