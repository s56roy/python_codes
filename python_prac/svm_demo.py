import numpy as np
import sklearn.svm as svm

#x = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
#y = np.array([1, 1, 2, 2])

#load training images

#preprocess them to get train_x and train_y

#load csv into x and y
x = np.loadtxt("~/Downloads/flowers.csv")


SVM = svm();
SVM.fit(x,y); #training
#blah


