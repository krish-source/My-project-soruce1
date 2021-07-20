
pip install -U -q PyDrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.
#redacted

#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm

dataset = pd.read_csv("Churn_Modelling.csv")

dataset.info()

dataset = dataset.iloc[:, 3:]

dataset.dtypes

pip install dataprep

from dataprep.eda import *

plot(dataset)

sns.pairplot(data=dataset, x_vars= ['Age', 'Balance', 'EstimatedSalary'], y_vars=['Exited'])

dataset = dataset[dataset['Age'] < 78]
dataset = dataset[dataset['Balance'] < 225000]
#removing outliers

sns.pairplot(data=dataset, x_vars= ['Age', 'Balance', 'EstimatedSalary'], y_vars=['Exited'])

dataset['EstimatedSalary'] = np.log(dataset['EstimatedSalary'])
# we transform the salary value to log form

dataset.head(5)

from dataprep.eda import plot_correlation

plot_correlation(dataset)

# isolating X and y variables

y = dataset.loc[:, 'Exited']
X = dataset.drop(['Exited'], axis=1)

X

# add constant

X = sm.add_constant(X)

X
#constant value added

#split dataset into training and test set
from sklearn.model_selection import train_test_split

X_Train, X_Test, y_Train, y_Test = train_test_split(X, y, test_size=0.2, random_state=1502)

# log regression & model fitting

model = sm.Logit(y_Train, X_Train).fit()
model.summary()

#predictions
predictions = model.predict(X_Test)
predictions = np.where(predictions > 0.1, 1, 0)

#Confusion matrix
from sklearn.metrics import classification_report
report = classification_report(y_Test, predictions)
print(report)

