import calendar
import csv
import pandas as pd
from io import BytesIO,TextIOWrapper
from io import TextIOWrapper

 # revenue_column = df['Revenue']
    # expenses_column = df['Expenses']
    # profit_column = df['Profit']
    # data_list = df.to_dict(orient='records')
    # data_list = df.to_dict(orient='records')
    # print(data_list)
    # print(revenue_column,expenses_column,profit_column)
def process_csv_file(file):
    df = pd.read_csv(file.file)
   
    columns_to_check = ['Month', 'Revenue', 'Expenses', 'Profit']
    
    if all(column in df.columns for column in columns_to_check):
        print("All columns exist.")
    else:
         missing_columns = [column for column in columns_to_check if column not in df.columns]
         return {'is_error':True,'error_message':f"Missing columns: {missing_columns}"}
     
    valid_months = list(calendar.month_name)[1:]
    invalid_months = df[~df['Month'].isin(valid_months)]
    
    if not invalid_months.empty:
        return {'is_error':True,'error_message':f"Missing columns: {missing_columns}"}
    else:
        print("All months are valid.")
        
    columns_to_check_num = ['Revenue', 'Expenses', 'Profit']
    for column in columns_to_check_num:
        try:
            df[column] = pd.to_numeric(df[column])
        except Exception as e:
            print(f"Error: The values in the '{column}' column are not numeric.")
            return {'is_error':True,'error_message':f"Error: The values in the '{column}' column are not numeric."}
           
        
    duplicates = df.duplicated(subset=['Month'])
    if any(duplicates):
        duplicate_months = df.loc[duplicates, 'Month']
        print(f"Duplicate months found: {duplicate_months.tolist()}")
    else:
        print("No duplicate months.")
        
        
    missing_months = set(valid_months) - set(df['Month'])
    missing_df = pd.DataFrame({'Month': list(missing_months), 'Revenue': 0, 'Expenses': 0, 'Profit': 0})
    df = pd.concat([df, missing_df], ignore_index=True)
    df['Month'] = pd.Categorical(df['Month'], categories=valid_months, ordered=True)
    df = df.sort_values(by='Month')
    
    print(df)
