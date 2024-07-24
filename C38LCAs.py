# This code plots the C38 alkenone compounds of GGC18 core

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the Excel file
file_path = "C:\\Users\olawa\Downloads\plot_data.xls"  # Replace with your file path
sheet_name = 'C38'  # Replace with your sheet name if necessary

# Read the data into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Select the columns you want to plot
columns_to_plot = ['C38:4Me', 'C38:4Et', 'C38:3bMe', 'C38:3bEt', 'C38:2Me', 'C38:2Et']  # Replace with your column names

# Plot the data
plt.figure(figsize=(10, 6))

for column in columns_to_plot:
    plt.plot(df.index, df[column], label=column)

# Customize the plot
plt.xlabel('Index')  # Replace with your x-axis label if necessary
plt.ylabel('Value')  # Replace with your y-axis label if necessary
plt.title('Line Plot of Selected Columns')
plt.legend()
plt.grid(False)

# Show the plot
plt.show()
