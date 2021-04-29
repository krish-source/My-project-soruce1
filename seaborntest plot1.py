import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


db = pd.read_csv('idle.csv', index_col=0)
sns.relplot(x="Agent", y="Till date", data=db, kind="line")
plt.show()
