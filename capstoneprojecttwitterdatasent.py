# -*- coding: utf-8 -*-


pip install -U -q PyDrive

#Auth Gdrive api
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.


link = 'https://drive.google.com/file/d/1bV3IBb-0GuwhbRMrbwVk26H9kvXUdRjb'

file_obj = drive.CreateFile({'id': '1bV3IBb-0GuwhbRMrbwVk26H9kvXUdRjb'})
file_obj.GetContentFile('training.1600000.processed.noemoticon.csv')

file_obj

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'

cols = ['sentiment','id','date','query_string','user','text']

df = pd.read_csv("training.1600000.processed.noemoticon.csv", header=None, names=cols, encoding="ISO-8859-1")

# we use encoding="ISO-8859-1" to load the csv file to a df since utf failed to encode.

df.head(5)

df.info()

df.sentiment

"""Dataset has 1.6million entries, with no null entries, and importantly for the "sentiment" column, even though the dataset description mentioned neutral class, the training set has no neutral class. 50% of the data is with negative label, and another 50% with positive label. We can see there's no skewness on the class division.


"""

df.query_string.value_counts()

df.drop(["id", "query_string", "user", "date"], axis=1, inplace=True)

"""We drop the uneeded columns"""

df.head(5)

pip install dataprep

from dataprep.eda import plot
from dataprep.datasets import load_dataset

df

plot(df)

"""We move on to the data cleaning part"""

from dataprep.clean import clean_text

"""We use data prep to clean the text column.


"""

df1 = clean_text(df, "text")

"""Cleaned df1 displayed below"""

df1

from google.colab import files
df1.to_csv('cleanedtwitter.csv')

files.download("cleanedtwitter.csv")
