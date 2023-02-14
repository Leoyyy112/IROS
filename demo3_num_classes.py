import numpy as np
import os
from PIL import Image

# Create a dictionary to map the old values to new values
value_map = {0:0, 10:1, 20:2, 30:3}

# Path to the folder containing the PNG files
input_folder = '/Users/liuyang/IROS-Segmentation/instrument_1_4_training/instrument_dataset_1/ground_truth/Right_Prograsp_Forceps_labels'

# Path to the folder where you want to store the new PNG files
output_folder = '/Users/liuyang/IROS-Segmentation/instrument_1_4_training/instrument_dataset_1/ground_truth/Right_Prograsp_Forceps_labels_num'

# Loop through all the PNG files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        # Load the PNG file as a numpy array
        img = np.array(Image.open(os.path.join(input_folder, filename)))

        # Replace the old values with the new values using the value_map dictionary
        img = np.vectorize(lambda x: value_map.get(x, x))(img)

        # Save the new PNG file in the output folder
        img = img.astype(np.uint8)
        Image.fromarray(img).save(os.path.join(output_folder, filename))

