#%%
"""
The script below extracts the tables of interest from the ASCII files of our stay at PSI. The resulting files are stores in the folder 'Data Selection'. 
Down below you find an example of how to use the files for data analysis.
"""

#%%
import pandas as pd
import glob
import os


def extract_tables():
    file_list = glob.glob("20211480/*")

    for file in file_list:
        measurement = file[-7:-4]

        # Reading the table in the ASCII file
        selected_lines = []
        data_trigger = False
        with open(file, 'r') as f:
            for line in f:
                if 'PNT' in line:
                    data_trigger = True
                if data_trigger:
                    selected_lines.append(line)

        # Writing the selected data in the new folder
        completeName = os.path.join('Data Selection', measurement + ' selected.csv')
        with open(completeName, 'w') as f:
            for item in selected_lines:
                f.write(item)


if __name__ == '__main__':
    extract_tables() # Carries out the conversion of the ASCII files to the selected data. You only have to run this once.


    # Example on how to use the data:
    measurement = 105 # Insert here the measurement of choice, e.g. numbers between 68 and 108

    # Using the selected data as a pandas DataFrame.
    data_pd = pd.read_csv('Data Selection/' + measurement + ' selected.csv', header = 0, skipinitialspace=True, sep=' ').iloc[:, :-1]
    print(f"Pandas DataFrame: ", '\n',  data_pd, data_pd.shape)

    # If you're not familiar with pandas, convert to a numpy array and use it from here on.
    data_np = data_pd.to_numpy()
    print("Numpy Array:", '\n', data_np, data_np.shape)

