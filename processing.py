from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import matplotlib as plt

data = pd.read_csv("training-set.csv", sep=";")
print(data.head())