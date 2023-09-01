import os
import pandas as pd

def combine_csv_files_in_folder(data_folder_path="."):
    """
    Combines multiple CSV files in a given folder and save the combined data, grouped by year, in a new folder.
    
    Parameters:
    - data_folder_path (str): Path to the folder containing the CSV files. Default is the current working directory.
    """
    
    combined_folder_path = "combined_data"
    
    # Create the new folder if it doesn't exist
    if not os.path.exists(combined_folder_path):
        os.makedirs(combined_folder_path)
    
    # List all the files in the data folder
    files_in_data_folder = os.listdir(data_folder_path)
    
    # Initialize an empty DataFrame to store the combined data
    combined_df = pd.DataFrame()
    
    # Iterate over the files
    for file_name in files_in_data_folder:
        if file_name.endswith('.csv'):
            # Extract the year from the file name
            year = int(file_name.split('_')[0])
            
            # Read the file into a DataFrame
            file_path = os.path.join(data_folder_path, file_name)
            df = pd.read_csv(file_path)
            
            # Add a 'Year' column to the DataFrame and set it to the extracted year
            df['Year'] = year
            
            # Concatenate the DataFrame to the combined DataFrame
            combined_df = pd.concat([combined_df, df])
    
    # Save each combined DataFrame to a new CSV file in the combined folder
    for year, year_df in combined_df.groupby('Year'):
        year_combined_file_path = os.path.join(combined_folder_path, f"{year}_combined_data.csv")
        year_df.to_csv(year_combined_file_path, index=False)
        print(f"Combined data for {year} saved to {year_combined_file_path}.")


if __name__ == "__main__":
    # Call the function to combine CSV files in the current working directory
    combine_csv_files_in_folder()