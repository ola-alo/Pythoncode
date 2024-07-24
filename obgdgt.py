import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
from matplotlib.font_manager import FontProperties


# Read data from Excel file
file_path = 'C:\\Users\olawa\Downloads\plot_data.xls'  # replace with your Excel file path
sheet_name = 'ob-gdgt'    # replace with your sheet name if necessary
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure the data has the required format
# Assuming the data has columns: 'X', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'
if not all(col in data.columns for col in ['Age', 'OB-GDGT-1064', 'OB-GDGT-1078', 'OB-GDGT-1092', 'OB-GDGT-1106',
                                           'OB-GDGT-1120', 'OB-GDGT-1134']):
    raise ValueError('The Excel file must contain columns: Age, OB-GDGT-1064, OB-GDGT-1078, OB-GDGT-1092, OB-GDGT-1106, OB-GDGT-1120, OB-GDGT-1134')

# Plotting the area plot
plt.figure(figsize=(10, 6))
plt.stackplot(data['Age'], data['OB-GDGT-1064'], data['OB-GDGT-1078'], data['OB-GDGT-1092'], data['OB-GDGT-1106'],
              data['OB-GDGT-1120'],data['OB-GDGT-1134'],
              labels=['OB-GDGT-1064', 'OB-GDGT-1078', 'OB-GDGT-1092', 'OB-GDGT-1106',
                                           'OB-GDGT-1120', 'OB-GDGT-1134'],
              colors=['#FFC0CB', '#00FF00', '#0000ff', '#FFFF00', '#000000', '#A52A2A'])

# Customizing the plot
#plt.legend(loc='best') # This controls the location of the legend
plt.title(' ') # Specify any title for the plot here
#plt.xlabel('Age (ka)')  # replace with appropriate label
#plt.ylabel('% Relative Contribution')  # replace with appropriate label

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


ax.xaxis.set_major_locator(MultipleLocator(2))  # Set x-axis tick interval to 10
ax.yaxis.set_major_locator(MultipleLocator(20))  # Set y-axis tick interval to 50


# The save the plot
plt.savefig('obgdgt.png')

# Show plot
plt.show()
