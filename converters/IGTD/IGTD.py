import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#import cv2
#from google.colab.patches import cv2_imshow
#from google.colab import drive
import Scripts.IGTD_Functions as igtd
import pickle

# Clone git repository and browse there
# !git clone 'https://github.com/zhuyitan/IGTD'
# !cd IGTD/

def run_igtd(dataset, rows, cols, result_dir):
    # Set parameters
    norm_data = igtd.min_max_transform(dataset.values)
    norm_data = pd.DataFrame(norm_data, columns=dataset.columns, index=dataset.index)
    num_row = rows
    num_col = cols
    num = num_row * num_col
    save_image_size = 10
    max_step = 1000
    val_step = 100
    fea_dist_method = 'Euclidean'
    image_dist_method = 'Euclidean'
    error = 'squared'
    switch_t = 0
    min_gain = 0.00001
    os.makedirs(name=result_dir, exist_ok=True)
    igtd.table_to_image(norm_data, [num_row, num_col], fea_dist_method, image_dist_method, save_image_size,
                        max_step, val_step, result_dir, error, switch_t, min_gain)
    return None

# Load datasets
X_train = pd.read_csv(r'datasets\tabular\X_train.csv', sep=';')
X_test = pd.read_csv(r'datasets\tabular\X_test.csv', sep=';')

# Modify datasets
X_train[0] = 0
X_train[1] = 0
X_train[2] = 0
X_test[0] = 0
X_test[1] = 0
X_test[2] = 0

# Run IGTD on Train set
result_dir = "datasets/images/Train"
run_igtd(dataset = X_train, rows = 8, cols = 8, result_dir = result_dir)

# Run IGTD on Test set
result_dir = "datasets/images/Test"
run_igtd(dataset = X_test, rows = 8, cols = 8, result_dir = result_dir)

"""
# Visualize
dir = 'Tabular data sets/Syphilis/y_train.csv'
y_train = pd.read_csv(dir, sep=';')

dir = '/IGTD/Datasets/Syphilis/Train/Results.pkl'
data = []
with open(dir, "rb") as file:
    for i in range(0, 3):
        data.append(pickle.load(file))

data = np.moveaxis(data[1], 2, 0)
data = np.expand_dims(X_train, 3)

# Extract the two images you want to plot
image1 = data[0]
image2 = data[1]

# Reshape the images if needed
image1 = np.reshape(image1, (8, 8))
image2 = np.reshape(image2, (8, 8))

# Plot the two images
fig, ax = plt.subplots(1, 2, figsize=(10, 10))
ax[0].imshow(image1, cmap='gray_r')
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[1].imshow(image2, cmap='gray_r')
ax[1].set_xticks([])
ax[1].set_yticks([])
plt.tight_layout()
plt.show()
"""