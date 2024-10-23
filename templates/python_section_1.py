from typing import Dict, List

import pandas as pd


def reverse_in_groups(lst, n):
    result = []
    i = 0

    while i < len(lst):
        group = []
        # reversing the group of n elements
        for j in range(min(n, len(lst) - i)):
            group.append(lst[i + j])
        
        # Appening reversed group to the result
        for k in range(len(group) - 1, -1, -1):
            result.append(group[k])
        
        i += n
    
    return result
    # Test examples
print(reverse_in_groups([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [3, 2, 1, 6, 5, 4, 8, 7]
print(reverse_in_groups([1, 2, 3, 4, 5], 2))          # Output: [2, 1, 4, 3, 5]
print(reverse_in_groups([10, 20, 30, 40, 50, 60, 70], 4))  # Output: [40, 30, 20, 10, 70, 60, 50]


------------------------------


def group_by_length(strings):
    length_dict = {}
    
    # Grouping the  strings by their length
    for string in strings:
        length = len(string)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(string)
    
    # Sorting the dictionary by key (length of strings)
    sorted_dict = dict(sorted(length_dict.items()))
    
    return sorted_dict
    # Example 
input_list1 = ["apple", "bat", "car", "elephant", "dog", "bear"]
output1 = group_by_length(input_list1)
print(output1)  # {3: ['bat', 'car', 'dog'], 4: ['bear'], 5: ['apple'], 8: ['elephant']}

input_list2 = ["one", "two", "three", "four"]
output2 = group_by_length(input_list2)
print(output2)  # {3: ['one', 'two'], 4: ['four'], 5: ['three']}

------------------------------------


def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            # Recursively flatten dictionaries
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            # If the value is a list, loop through the list elements
            for i, item in enumerate(v):
                items.extend(flatten_dict({f"{k}[{i}]": item}, parent_key, sep=sep).items())
        else:
            # Otherwise, it's a base value, so add it as is
            items.append((new_key, v))
    return dict(items)

# Example by assessement
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                } 
            }
        ]
    }
}

flat_dict = flatten_dict(nested_dict)
print(flat_dict)

-----------------------------------------
def permute_unique(nums):
    result = []
    nums.sort()  # Sorting the list to make  skip duplicates
    visited = [False] * len(nums)
# using backtrack to searching through all possible options

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])  # Append a copy of the current path
            return
        
        for i in range(len(nums)):
            # Skipiing the duplicates: 
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            path.append(nums[i])

            backtrack(path)

            path.pop()  # Backtrack
            visited[i] = False

    backtrack([])
    return result

# example by assessment
input_list = [1, 1, 2]
print(permute_unique(input_list))

----------------------
import re

def find_all_dates(text):
    #Using regalar expressions for the three date formats
    patterns = [
     r'\b\d{2}-\d{2}-\d{4}\b',  # dd-mm-yyyy
        r'\b\d{2}/\d{2}/\d{4}\b',  # mm/dd/yyyy
        r'\b\d{4}\.\d{2}\.\d{2}\b'  # yyyy.mm.dd
    ]
    
   # Combining all patterns  with OR (|) and search in the text

    combined_pattern = '|'.join(patterns)
    
    # Finding all matches
    matches = re.findall(combined_pattern, text)
    
    return matches

# Example 
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
print(find_all_dates(text))

----------------------------
import polyline  #polyline to decode the polyline string into latitude and longitude pairs.
import pandas as pd  #pandas to create and manipulate the DataFrame.
from math import radians, cos, sin, sqrt, atan2  #math for calculating distances using the Haversine formula.

def haversine(lat1, lon1, lat2, lon2): #using haversine to find distace between two points on a sphere
   
    R = 6371000  # Radius of the Earth in meters
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c  # Distance in meters
    return distance

def decode_polyline_to_df(polyline_str):
    # Decode the polyline string into a list of (latitude, longitude) tuples
    coordinates = polyline.decode(polyline_str)

    # Create a Pandas DataFrame
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])

    # Initialize the distance column with 0 for the first row
    df['distance'] = 0.0

    # Calculating the distance between successive points
    for i in range(1, len(df)):
        lat1, lon1 = df.loc[i - 1, 'latitude'], df.loc[i - 1, 'longitude']
        lat2, lon2 = df.loc[i, 'latitude'], df.loc[i, 'longitude']
        df.loc[i, 'distance'] = haversine(lat1, lon1, lat2, lon2)

    return df

# Example 
polyline_str = "_p~iF~ps|U_ulLnnqC_mqNvxq`@"
df = decode_polyline_to_df(polyline_str)
print(df)



-----------------------------
def rotate_and_transform(matrix):
    n = len(matrix)
    
    # Rotate the matrix by 90 degrees clockwise
    # Transpose the matrix and reverse each row
    rotated_matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]
    rotated_matrix = [row[::-1] for row in rotated_matrix]
    
    # Create a new matrix to store the final result
    final_matrix = [[0] * n for _ in range(n)]
    
    # Precompute row sums and column sums for the rotated matrix
    row_sums = [sum(row) for row in rotated_matrix]
    col_sums = [sum(rotated_matrix[i][j] for i in range(n)) for j in range(n)]
    
    #Replace each element in the rotated matrix with the sum of its row and column, excluding itself
    for i in range(n):
        for j in range(n):
            final_matrix[i][j] = row_sums[i] + col_sums[j] - 2 * rotated_matrix[i][j]
    
    return final_matrix

# given example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
final_matrix = rotate_and_transform(matrix)
for row in final_matrix:
    print(row)



------------------------------
import pandas as pd

def check_timestamp_completeness(df):
    # Parse startDay, startTime, endDay, endTime into datetime objects
    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], format='%Y-%m-%d %H:%M:%S')
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], format='%Y-%m-%d %H:%M:%S')

    # Grouping by (id, id_2)
    grouped = df.groupby(['id', 'id_2'])

    def verify_coverage(group):
        # Get the unique days from startDay
        unique_days = pd.to_datetime(group['startDay']).dt.dayofweek.unique()

        # Checking if all 7 days of the week are covered (Monday=0, Sunday=6)
        seven_day_span = set(unique_days) == set(range(7))

        # Checking if the 24-hour span is covered for each day
        day_coverage = {}
        for _, row in group.iterrows():
            start_time = row['start_datetime']
            end_time = row['end_datetime']
            
            # Create a range for each day and check if 24 hours are covered
            current_day = start_time.date()
            if current_day not in day_coverage:
                day_coverage[current_day] = set()
                
            day_coverage[current_day].update(pd.date_range(start=start_time, end=end_time, freq='S').time)

        # Check if each day in day_coverage has a full 24-hour span (86400 seconds)
        full_day_coverage = all(len(times) == 86400 for times in day_coverage.values())

        return seven_day_span and full_day_coverage

    # Apply the check to each group and return a boolean series
    result = grouped.apply(verify_coverage)

    return result

# Example 
df = pd.read_csv('C:\\new\\dataset-2.csv')  #  loading the CSV as a DataFrame
result = check_timestamp_completeness(df)
print(result)


