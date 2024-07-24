import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
from matplotlib.font_manager import FontProperties


# Read data from Excel file
file_path = 'C:\\Users\olawa\Downloads\plot_data.xls'  # replace with your Excel file path
sheet_name = 'Phytoplanktons'    # replace with your sheet name if necessary
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure the data has the required format
# Assuming the data has columns: 'X', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'
if not all(col in data.columns for col in ['Age', 'Chl-a-DDs', 'LCAs']):
    raise ValueError('The Excel file must contain columns: Age, Chl-a-DDs, LCAs,')

# Plotting the area plot
plt.figure(figsize=(10, 6))
plt.stackplot(data['Age'], data['Chl-a-DDs'], data['LCAs'],
              labels=['Chl-a-DDs', 'LCAs'],
              colors=['#00FF00', '#0000ff'])

# Customizing the plot
#plt.legend(loc='best') # This controls the location of the legend
plt.title(' ') # Specify any title for the plot here
#plt.xlabel('Age (ka)')  # replace with appropriate label
#plt.ylabel('% Relative Contribution')  # replace with appropriate label

# To remove grid lines
plt.grid(False)

# To customize the plot axes ranges
plt.xlim(0, 16.5)
plt.ylim(80, 100)

# To customize tick orientation
plt.xticks(rotation=90)
plt.yticks(rotation=90)


# Formatting tick labels to specific decimal places
ax = plt.gca() # Get current axes
ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f')) # Formats x-axis tick label to 0 decimal place
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f')) # Formats y-axis tick label to 0 decimal place


ax.xaxis.set_major_locator(MultipleLocator(2))  # Set x-axis tick interval to 10
ax.yaxis.set_major_locator(MultipleLocator(5))  # Set y-axis tick interval to 50


# The save the plot
plt.savefig('phytoplankton.png')

# Show plot
plt.show()
