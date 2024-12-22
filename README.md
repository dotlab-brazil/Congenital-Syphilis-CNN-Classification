# The use of Convolutional Neural Network to classify Congenital Syphilis with image representations of tabular data
## Abstract
Although CNNs are primarily designed for image analysis, they can also be adapted to work with tabular data. This can be achieved by first converting the tabular data into images, enabling their use with image models. Several tools have been proposed in the literature to convert tabular data into images to improve classification performance. Techniques that enhance classification performance are especially valuable in complex problems such as the classification of Congenital Syphilis (CS). This work specifically aims to compare the performance of a traditional Machine Learning (ML) algorithm and simple Convolutional Neural Networks (CNNs) in classifying CS using a dataset composed of tabular data. We evaluate the performance of various methods for transforming tabular data into image representations and selected the conversion technique where the CNN achieved the highest metrics. Additionally, the CNN model was optimized using Random Search and compared to the performance of an optimized ML algorithm, Adaboost. The results indicate that CNNs can perform similarly to traditional ML algorithms when classifying images generated from CS tabular data, highlighting the potential of CNNs for improved medical data analysis.

## Methogology
<div align='center'>
<img src="Images/methodology.png" alt="Methodology" width="900"/>
</div>

## Summary of Results

### Results of the Basic CNNs
![Results of the Basic CNNs](Images/basic_cnns.png)
### Results of the Tuned CNN
![Results of the Tuned CNN](Images/tuned_cnns.png)

### Training x validation accuracy and loss of the Tuned-Deepinsight-CNN across epochs

<div align="center">
<img src="Images/Tuned-Deepinsight-CNN_train_val_acc.png" alt="Training x validation accuracy of the Tuned-Deepinsight-CNN across epochs" width="400" style="display:inline-block; margin-right: 10px;"/>
<img src="Images/Tuned-Deepinsight-CNN_train_val_loss.png" alt="Training x validation loss of the Tuned-Deepinsight-CNN across epochs" width="400" style="display:inline-block;"/>
</div>

### Confusion matrix of the Tuned-Deepinsight-CNN
<div align="center">
<img src="Images/Tuned-Deepinsight-CNN_confusion_matrix.png" alt="Confusion matrix of the Tuned-Deepinsight-CNN" width="400"/>
</div>

## Steps to reproduce the experiments
To reproduce the experiments, you can run the jupyter notebooks locally or on google collab. For that, please follow the steps below:

1. Clone this  repository
```bash
git clone https://github.com/dotlab-brazil/Congenital-Syphilis-CNN-Classification
```
2. Clone the repositories of each converter for tabular data into images
```bash
git clone https://github.com/alok-ai-lab/pyDeepInsight
git clone https://github.com/zhuyitan/IGTD
git clone https://github.com/omidbazgirTTU/REFINED
```

3. Install the requirements
```bash
pip install -r requirements.txt
```

4. Run the jupyter notebooks

**If you are in google colab:** 
1. Upload the jupyter notebooks to your google drive
2. Open the jupyter notebooks in google collab
3. Mount your google drive
```python
from google.colab import drive
drive.mount('/content/drive')
```
4. Clone the repos for each technique
5. Install the required libraries (replace the path with the path where the requirements.txt is located in your drive)
```bash	
!pip install -r /content/drive/MyDrive/~/requirements.txt
```	
6. Run the jupyter notebooks

