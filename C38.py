import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the Excel file
file_path = 'C:\\Users\olawa\Downloads\plot_data.xls'  # Replace with your file path
sheet_name = 'C38'  # Replace with your sheet name if necessary

# Read the data into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Select the columns you want to plot
columns_to_plot = ['C38:4Me', 'C38:4Et', 'C38:3bMe', 'C38:3bEt', 'C38:2Me', 'C38:2Et']  # Replace with your column names

# Create subplots
num_plots = len(columns_to_plot)
fig, axs = plt.subplots(num_plots, 1, figsize=(10, num_plots * 4), sharex=True)

for i, column in enumerate(columns_to_plot):
    axs[i].plot(df.index, df[column], label=column)
    axs[i].set_title({column})
    axs[i].set_ylabel('ug/g OC')  # Replace with your y-axis label if necessary
    axs[i].grid(False)
    #axs[i].legend()

# Set the x-axis label for the last subplot
axs[-1].set_xlabel('Age (ka)')  # Replace with your x-axis label if necessary

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
