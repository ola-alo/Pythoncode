import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator

# Read data from Excel file
file_path = 'C:\\Users\olawa\Downloads\plot_data.xls'  # replace with your Excel file path
sheet_name = 'Alkenone-total'    # replace with your sheet name if necessary
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure the data has the required format
# Assuming the data has columns: 'X', 'Y1', 'Y2', 'Y3', 'Y4'
if not all(col in data.columns for col in ['Age', 'C37', 'C38', 'C39', 'C40']):
    raise ValueError('The Excel file must contain columns: Age, C37, C38, C39, C40')

# Plotting the area plot
plt.figure(figsize=(10, 6))
plt.stackplot(data['Age'], data['C37'], data['C38'], data['C39'], data['C40'],
              labels=['%C37', '%C38', '%C39', '%C40'],
              colors=['#FFC0CB', '#00FF00', '#0000ff', '#FFFF00'])

# Customizing the plot
#plt.legend(loc='lower left') # This controls the location of the legend
plt.title(' ') # Specify any title for the plot here
plt.xlabel('')  # replace with appropriate label
plt.ylabel('')  # replace with appropriate label

# To remove grid lines
plt.grid(False)

# To customize the plot axes ranges
plt.xlim(0, 16.5)
plt.ylim(0, 100)

# To customize tick orientation
plt.xticks(rotation=90)
plt.yticks(rotation=90)

# Formatting tick labels to specific decimal places

ax = plt.gca() # Get current axes
ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f')) # Formats x-axis tick label to 0 decimal place
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f')) # Formats y-axis tick label to 0 decimal place

# Set custom tick intervals
ax.xaxis.set_major_locator(MultipleLocator(2))  # Set x-axis tick interval to 10
ax.yaxis.set_major_locator(MultipleLocator(20))  # Set y-axis tick interval to 50

# The save the plot
plt.savefig('lca.png')

# Show plot
plt.show()



