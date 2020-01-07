# library
# libraries
import seaborn as sns
import pandas as pd
import numpy as np
 
# create dataset
#df = np.random.randn(30, 30)
#df = np.array([[1, 4], [2, 5],[3, 6]])
df = np.zeros([100, 100])
# create heatmap
sns.heatmap(df, cmap="Blues")
sns.plt.show()
