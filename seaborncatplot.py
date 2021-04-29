import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


b = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", data=b)
plt.show()
