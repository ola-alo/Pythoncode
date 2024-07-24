import pandas as pd
import xlrd
import matplotlib.pyplot as plt
import numpy as np


location = ('C:\\Users\olawa\Downloads\plot_data.xls')

sheet_name = 'Sheet2'
df = pd.read_excel(location, sheet_name=sheet_name)

# The first column (Age) is set as the index and other columns are data series
x = df.set_index(df.columns[0], inplace=True)

#Define the data set


chl_a = df['Chl-a-DDs']
lca = df['LCA']
cren = df['Cren']
obgdgt = df['OB-GDGT']
dages = df['DAGEs']

# Define the colors if you don't want the default colors

colors = ['pink', 'blue', 'yellow', 'black', 'deep brown']


# Create the plot

plt.fill_between(x, chl_a, color=colors[0], alpha=0.5, label='Chl-a-DDs')
plt.fill_between(x, lca, chl_a, color=colors[1], alpha=0.5, label='LCA')
plt.fill_between(x, cren, lca, color=colors[2], alpha=0.5, label='Cren')
plt.fill_between(x, obgdgt, cren, color=colors[3], alpha=0.5, label='OB-GDGT')
plt.fill_between(x, dages, obgdgt, color=colors[4], alpha=0.5, label='DAGEs')


# Title and labels
plt.title("Relative Abundance (%)")
plt.xlabel("Age (ka)")
#plt.ylabel("%")

# Create the area plot

df.plot(kind='area', alpha=0.5)

plt.legend(loc='best')
plt.tight_layout()
plt.show()



