def validate_missing_values(dataframe, threshold=0.1):
    """
    Validate missing values in the dataframe.
    
    Parameters:
    dataframe (pd.DataFrame): The dataframe to validate.
    threshold (float): The threshold for missing values (default is 10%).
    
    Returns:
    dict: A dictionary with columns as keys and percentage of missing values as values.
    """
    missing_percentage = dataframe.isnull().mean() * 100
    return missing_percentage[missing_percentage > threshold].to_dict()


def validate_data_types(dataframe, expected_types):
    """
    Validate data types of the dataframe columns.
    
    Parameters:
    dataframe (pd.DataFrame): The dataframe to validate.
    expected_types (dict): A dictionary with column names as keys and expected data types as values.
    
    Returns:
    dict: A dictionary with columns as keys and a boolean indicating if the type matches as values.
    """
    type_validation = {col: dataframe[col].dtype == expected_types[col] for col in expected_types}
    return type_validation


def validate_unique_values(dataframe, column):
    """
    Validate unique values in a specific column of the dataframe.
    
    Parameters:
    dataframe (pd.DataFrame): The dataframe to validate.
    column (str): The column name to check for unique values.
    
    Returns:
    bool: True if all values are unique, False otherwise.
    """
    return dataframe[column].is_unique


def run_data_validations(dataframe, expected_types, unique_columns):
    """
    Run all data validations on the dataframe.
    
    Parameters:
    dataframe (pd.DataFrame): The dataframe to validate.
    expected_types (dict): A dictionary with expected data types for validation.
    unique_columns (list): A list of columns that should have unique values.
    
    Returns:
    dict: A dictionary with validation results.
    """
    results = {}
    results['missing_values'] = validate_missing_values(dataframe)
    results['data_types'] = validate_data_types(dataframe, expected_types)
    
    for column in unique_columns:
        results[f'unique_{column}'] = validate_unique_values(dataframe, column)
    
    return results