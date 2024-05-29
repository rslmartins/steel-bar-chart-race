import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import bar_chart_race as bcr
# Load data from World Steel
"""
https://worldsteel.org/wp-content/uploads/Steel-Statistical-Yearbook-1980.pdf
https://worldsteel.org/wp-content/uploads/Steel-Statistical-Yearbook-1990.pdf
https://worldsteel.org/wp-content/uploads/Steel-Statistical-Yearbook-2000.pdf
https://worldsteel.org/wp-content/uploads/Steel-Statistical-Yearbook-2010.pdf
https://worldsteel.org/wp-content/uploads/Steel-Statistical-Yearbook-2020-concise-version.pdf
"""
# Define the Excel file and the sheet names
excel_file = 'data.xlsx'
sheet_names = ['Sheet1', 'Sheet2', 'Sheet3', 'Sheet4', 'Sheet5']
# Initialize an empty list to hold the data frames
dfs = []
# Loop through each sheet name and read it into a data frame
for sheet in sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet, index_col=0)
    dfs.append(df)
# Concatenate all data frames into a single one
df = pd.concat(dfs, axis=1)
# Create video
bcr.bar_chart_race(
        df=df.fillna(0.0).T,
        filename='steel.mp4',
        fixed_max=True,
        fixed_order=False,
        n_bars=20,
        steps_per_period=10,
        interpolate_period=False, 
        period_length=800,
        orientation='h',
        bar_size=.95,
        scale='linear',
        filter_column_colors=True,
        period_summary_func=lambda v, r: {'x': .98, 'y': .2, 
                                          's': f'Total world production: {v.sum():,.0f}', 
                                          'ha': 'right', 'size': 11}, 
        title="Steel production by country in thousand metric tons (1969 to 2019)")
