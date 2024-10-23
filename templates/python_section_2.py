import pandas as pd



import pandas as pd

def calculate_distance_matrix(file_path):
    # Load the dataset
    df = pd.read_csv(file_path, index_col=0)
    
    for i in range(df.shape[0]):
        for j in range(i, df.shape[1]):
            if i == j:
                df.iloc[i, j] = 0  # Set diagonal values to 0
            else:
                # Symmetry: A to B should equal B to A
                df.iloc[j, i] = df.iloc[i, j]
    
    return df

# Call the function with the dataset path
distance_matrix = calculate_distance_matrix('C:\ \Users\\user\\Downloads\\dataset-2.csv')

# Display the result
print(distance_matrix)
-----------------------------------------



import pandas as pd

def unroll_distance_matrix(df):
    # Create a list to store the rows
    data = []
    
    # Iterate over the rows and columns of the DataFrame
    for id_start in df.index:
        for id_end in df.columns:
            if id_start != id_end:  # Skip diagonal values where id_start == id_end
                data.append([id_start, id_end, df.loc[id_start, id_end]])
    
    # Convert the list to a DataFrame
    unrolled_df = pd.DataFrame(data, columns=['id_start', 'id_end', 'distance'])
    
    return unrolled_df
# Call the function with the dataset path

unrolled_matrix = unroll_distance_matrix(distance_matrix) (' C:\ \Users\\user\\Downloads\\dataset-2.csv')                                   

# Display the result
print(unrolled_matrix)

---------------------------

def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here

    return df

----------------------------
def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here

    return df
----------------------------------------


