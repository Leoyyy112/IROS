import nibabel as nib
from PIL import Image
import numpy as np
filename = '/Users/liuyang/IROS-Segmentation/WSL4MIS-main/imgs/Prostatex_0000.nii.gz'
img = nib.load(filename)
shape = img.shape
print("The shape of the NIFTI file is:", shape)



filename = '/Users/liuyang/IROS-Segmentation/instrument_1_4_training/instrument_dataset_1/right_frames/frame000.png'
img = Image.open(filename)
img = np.array(img)
img = (img - img.min()) / (img.max() - img.min())#image
print(np.shape(img))
print(np.max(img))
print(np.min(img))
print(np.unique(img))


# # Original label image
# label_img = np.array([[0, 20, 30, 20, 0],
#                       [30, 20, 0, 20, 30]])
#
# # Find the unique values in the label image
# unique_vals, inverse = np.unique(label_img, return_inverse=True)
#
# # Map old values to new values
# new_vals = np.arange(len(unique_vals))
# mapping = {old: new for old, new in zip(unique_vals, new_vals)}
# new_label_img = np.vectorize(mapping.get)(label_img)
#
# # Verify that the image was converted correctly
# print(new_label_img)
# print(np.unique(new_label_img))



# num = 4
# print(tuple([1,num-1]))

