import os
import pandas as pd

def process_and_combine_csv_files(data_folder_path="."):
    """
    Combines multiple CSV files in a given folder based on certain criteria 
    and save the combined data to a new file.
    
    Parameters:
    - data_folder_path (str): Path to the folder containing the CSV files. 
                              Default is the current working directory.
    """

    # List of years for which you want to process files
    desired_years = ['2018', '2019', '2021', '2022', '2023']

    # List of airlines to filter
    desired_airlines = ['9E', 'OH', 'YV', 'QX', 'PT', 'ZW', 'G7', 'C5', 'EM', 'KS', '9K', 'AS', 'NK', 'F9', 'G4', 'HA']

    # Columns to extract
    columns = [
        'Year', 'Month', 'DayOfWeek', 'Operating_Airline', 'Tail_Number',
        'Origin', 'OriginState', 'Dest', 'DestState', 'DepDelayMinutes', 
        'DepDel15', 'DepTimeBlk', 'TaxiOut', 'WheelsOff', 'WheelsOn', 'TaxiIn',
        'ArrDel15', 'ArrDelayMinutes', 'ArrTimeBlk', 'Distance',
        'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'DistanceGroup'
    ]

    # Initialize an empty DataFrame to store the combined data
    combined_df = pd.DataFrame()

    # Iterate over the files
    for file_name in os.listdir(data_folder_path):
        if file_name.endswith('.csv'):
            print("Processing file:", file_name)
            parts = file_name.split('_')
            year = parts[0]
            month = int(parts[1])  # Convert month to integer
            
            if year in desired_years:
                if 1 <= month <= 12:
                    # Read the file into a DataFrame
                    file_path = os.path.join(data_folder_path, file_name)
                    df = pd.read_csv(file_path)
                    
                    # Filter by desired airlines
                    df = df[df['Operating_Airline'].isin(desired_airlines)]
                    
                    # Extract only the desired columns
                    df = df[columns]
                    
                    # Add 'Year' and 'Month' columns to the DataFrame
                    df['Year'] = year
                    df['Month'] = month
                    
                    # Concatenate the DataFrame to the combined DataFrame
                    combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Save the combined data to a new CSV file
    combined_data_file = os.path.join(data_folder_path, 'combined_data_mkt.csv')
    combined_df.to_csv(combined_data_file, index=False)

    print(f"Combined data saved to {combined_data_file}")

if __name__ == "__main__":
    # Call the function to process and combine CSV files in the current working directory
    process_and_combine_csv_files()
