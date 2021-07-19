

pip install -U -q PyDrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.
#[redacted]


import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm

df3 = pd.read_csv('houses_to_rent.csv')

df3

df3.info()

pip install dataprep

from dataprep.eda import *

plot(df3)

# Reduction columns to "city", "area", "rooms", "bathroom","parking spaces", "floor", "animal", "furniture", "rent amount"
dataset = df3.loc[:, ["city", "area", "rooms", "bathroom", "parking spaces", "floor", "animal", "furniture", "rent amount"]]
print("Extra columns deleted")

dataset.info()

#transforming animal and furniture to numerical values

dataset[["animal", "furniture"]] = pd.get_dummies(dataset[["animal", "furniture"]], drop_first = True)

dataset["floor"] = np.where(dataset["floor"] == '-', '0', dataset["floor"])

dataset.info()

dataset["floor"] = dataset["floor"].astype(int)
#changing floor value from object to integer

dataset.info()

# We have to change the rent amount from object to float or numrical  value and remove currency symbols in order to further analysis

dataset["rent amount"] = dataset["rent amount"].str.replace('R', '')
dataset["rent amount"] = dataset["rent amount"].str.replace('$', '')
dataset["rent amount"] = dataset["rent amount"].str.replace(',', '')

# converting value ot float

dataset["rent amount"] = dataset["rent amount"].astype(float)

dataset.info()

dataset.describe()

plot(dataset)

from dataprep.eda import plot_correlation

plot_correlation(dataset)

#plotting continuous variables against the dependent variable
sns.pairplot(data = dataset,
             x_vars = ['area', 'rooms', 'bathroom',
                       'parking spaces', 'floor'],
             y_vars = ['rent amount'])

#remove outliers
dataset = dataset[dataset["area"] < 1500]
dataset = dataset[dataset["floor"] < 30]
dataset = dataset[dataset["rent amount"] < 16000]

#plotting continuous variables against the dependent variable
sns.pairplot(data = dataset,
             x_vars = ['area', 'rooms', 'bathroom',
                       'parking spaces', 'floor'],
             y_vars = ['rent amount'])

plot_correlation(dataset)

# We have high correlation for rooms and parking spaces so we remove 

dataset = dataset.drop(['rooms', 'parking spaces'], axis=1)

plot_correlation(dataset)

#transfor variables into their log form
dataset['rent amount'] = np.log(dataset['rent amount'])
dataset['area'] = np.log(dataset['area'])

dataset.head(5)

#isolate X and Y variables
y = dataset.iloc[:, -1]
X = dataset.iloc[:, :-1]

#linear regression - fitting model
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
model.summary()

X

#create price for an aparment
apartment = [1, 1, np.log(85), 1, 4,0, 1]
apartment

#create price for an aparment
apartment = [1, 1, np.log(62), 1, 2, 0, 1]
price = model.predict(apartment)
price = np.exp(price)
print("The predicted price of apartment:", price)

