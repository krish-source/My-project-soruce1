import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


a = sns.load_dataset("flights")
sns.relplot(x="passengers", y="month", hue="year", data=a)
plt.show()
