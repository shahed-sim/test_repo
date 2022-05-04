import os
import time
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
from IPython.display import Markdown as md
import missingno as msno
from scipy import stats
from sklearn.impute import KNNImputer
from numpy import isnan
from matplotlib.pyplot import figure
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import make_classification


filepath = os.path.dirname(os.getcwd()) + '\PA_Traffic_Data_2001_to_2020'
print(filepath)

