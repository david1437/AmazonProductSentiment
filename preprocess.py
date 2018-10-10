import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def read_data(filename):
    return pd.read_csv(filename, header=None, index_col=None).iloc[:,:].values
