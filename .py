import numpy as np
import pandas as pd
import csv

# Creating arrays
x = np.arange(0, 10, 0.1)
y = x * 2
z = 3 * y - x
a = x + y
b = y - x
c = x + y + z

# Displaying arrays
print(f"Displaying array x:\n{x}\n\n")
print(f"Displaying array y:\n{y}\n\n")
print(f"Displaying array z:\n{z}\n\n")
print(f"Displaying array a:\n{a}\n\n")
print(f"Displaying array b:\n{b}\n\n")
print(f"Displaying array c:\n{c}\n\n")

# Creating dataframes
df1 = pd.DataFrame({"x": x, "y": y, "z": z})
df2 = pd.DataFrame({"a": a, "b": b, "c": c})

# Displaying dataframes
print(f"Displaying Dataframe 'df1' as:\n{df1}\n\n")
print(f"Displaying Dataframe 'df2' as:\n{df2}\n\n")

# Concatenate all dataframes
df_concatenated = pd.concat([df1, df2], ignore_index=True)

# Displaying concatenated dataframe
print(f"Displaying Concatenated Dataframe 'df_concatenated' as:\n{df_concatenated}\n\n")

# Creating csv file to store the data
csvfile = "csvfilerecorder0.csv"
try:
    with open(csvfile, 'w', newline='') as file:
        df_concatenated.to_csv(file, index=False)
    print(f"Data has been written to csv file {csvfile.upper()} successfully!\n\n")
except Exception as e:
    print(f"Error occurred while writing to csv file {csvfile.upper()}: {str(e)}")

# Dropping rows with empty cells
df_cleaned = df_concatenated.dropna()
print(f"Dropping rows with empty cells:\n{df_cleaned}\n")

# Displaying DataFrame info and description
info = df_cleaned.info()
describe = df_cleaned.describe()
print(f"Showing Information as below:\n{info}\n\n")
print(f"Showing Descriptions as below:\n{describe}\n\n")

# Removing duplicate rows
df_no_duplicates = df_concatenated.drop_duplicates()

# Creating 2nd csv file to store the data
csvfile = "csvfilerecorder02.csv"
try:
    with open(csvfile, 'w', newline='') as file:
        df_no_duplicates.to_csv(file, index=False)
    print(f"Data has been written to csv file {csvfile.upper()} successfully!\n\n")
except Exception as e:
    print(f"Error occurred while writing to csv file {csvfile.upper()}: {str(e)}")

# Count and print DataFrame properties
def print_dataframe_properties(df_no_duplicates):
    print(f"*\n**\n***\nDataFrame properties as below:\n\n")
    print(f"Number of rows: {len(df_no_duplicates)}\n")
    print(f"Number of columns: {len(df_no_duplicates.columns)}\n")
    print(f"Column names: {df_no_duplicates.columns.tolist()}\n")
    print(f"Data types:\n{df_no_duplicates.dtypes}\n")
    print(f"Number of non-null values:\n{df_no_duplicates.count()}\n")
    print(f"Number of unique values in each column:\n{df_no_duplicates.nunique()}\n")
    print(f"Summary statistics:\n{df_no_duplicates.describe()}\n")
    print(f"Top values in each column:\n{df_no_duplicates.head(1)}\n")

# Call the function with the DataFrame
print_dataframe_properties(df_no_duplicates)

# Store the properties in a doc file
docfile = "Dataframe_Properties001.doc"
try:
    with open(docfile, 'w') as file:
        print_dataframe_properties(df_no_duplicates)
    print(f"Properties have been written to a doc file {docfile.upper()} successfully!\n\n")
except Exception as e:
    print(f"Error occurred while writing to a doc file {docfile.upper()}: {str(e)}")

# Store the properties in a csv file
csv_file = "Dataframe_Properties001.csv"
try:
    with open(csv_file, 'w', newline='') as file:
        df_properties = df_no_duplicates.describe().transpose()
        df_properties.to_csv(file, index=False)
    print(f"Properties have been written to a CSV file {csv_file.upper()} successfully!\n\n")
except Exception as e:
    print(f"Error occurred while writing properties to a CSV file {csv_file.upper()}: {str(e)}")
