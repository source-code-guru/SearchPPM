"""
A small python script which extracts masses intensities in a DataAnalysis output +/- delta ppm
Author : Marc HAEGELIN
Date : 02-12-2023
"""


import os
import pandas as pd

# Define mass values and delta in ppm
mass_values = [829.459, 879.44228, 889.45106, 1079.55537, 1089.56368]
ppm = 2

# Compute deltas for each mass value
mass_deltas = {mass_value: (ppm / 1e6) * mass_value for mass_value in mass_values}

# Dictionary to store temporary results
temp_results = {}

# Iterate over all files in the folder
folder = "I:\\Bioinfo\\Recherche MS FTICR\\prediction\\"  # Replace with your folder path

for filename in os.listdir(folder):
    # Check if it's a CSV file
    if filename.endswith(".csv"):
        # Read the CSV file with Pandas
        df = pd.read_csv(os.path.join(folder, filename), delimiter=',')

        # Iterate over each mass value and its corresponding delta
        for mass_value, delta in mass_deltas.items():
            # Filter values relative to the mass value and delta
            filtered_values = df.loc[df['m/z'].between(mass_value - delta, mass_value + delta)]

            # Count the number of rows
            num_rows = len(filtered_values)

            # Set the default sum to 0
            total = 0

            # If the number of rows is greater than 0
            if num_rows > 0:
                # Compute the sum of values in the second column
                total = filtered_values[' I'].sum()

            # Add the value to the temporary list
            file_name = filename[:-4]  # Remove the .csv extension
            temp_results.setdefault(file_name, []).append(total)

# Create a DataFrame from the dictionary
df_results = pd.DataFrame.from_dict(temp_results, orient='index', columns=mass_deltas.keys())

# Transpose the DataFrame
df_result_transpose = df_results.transpose()

# Rename the columns with the file names
df_result_transpose.columns = temp_results.keys()

# Set the DataFrame index to the fixed values
df_result_transpose.index = df_result_transpose.index.map('{:.6f}'.format)  # Use 6 decimals for masses

# Define the output file name
output_file = "output.csv"

# Save the DataFrame as CSV
df_result_transpose.to_csv(output_file, index=True)
