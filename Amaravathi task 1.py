import pandas as pd

# Step 1: Load the CSV files
customers_df = pd.read_csv('C:\Harsha files\Customers.csv')
transactions_df = pd.read_csv('C:\Harsha files\Transaction.csv')
course_df = pd.read_csv('C:\Harsha files\Studies.csv')
courses_df = pd.read_csv('C:\Harsha files\Software.csv')

# Step 2: Merge the Customers and Transactions into a single dataframe
merged_df = pd.merge(customers_df, transactions_df, on='customer_id')

# Step 3: Calculate the duration in days between start date and end date
merged_df['start_date'] = pd.to_datetime(merged_df['start_date'], format='%d-%m-%Y')
merged_df['end_date'] = pd.to_datetime(merged_df['end_date'], format='mixed' ,errors='coerce')
merged_df['duration'] = (merged_df['end_date'] - merged_df['start_date']).dt.days

# Step 4: Drop the duplicate rows in the merged dataframe if any
merged_df.drop_duplicates(inplace=True)

# Step 5: Drop rows with missing values in the merged dataframe if any
merged_df.dropna(inplace=True)

# Step 6: Calculate the average duration of each customer
average_duration = merged_df.groupby('customer_id')['duration'].mean()

# Step 7: Display the unique transaction types
unique_transaction_types = merged_df['txn_type'].unique()

# Step 8: Display the count of each transaction type with respect to each continent
# Assuming region_id can be mapped to continents, we create a dummy mapping here
region_to_continent = {
    1: 'Asia',
    2: 'Europe',
    3: 'North America',
    4: 'South America',
    5: 'Australia',
    6: 'Africa'
}
merged_df['continent'] = merged_df['region_id'].map(region_to_continent)
transaction_type_count = merged_df.groupby(['continent', 'txn_type']).size()

# Step 9: Find out the selling cost average for packages developed in Pascal
pascal_avg_selling_cost = courses_df[courses_df['DEVELOPIN'] == 'PASCAL']['SCOST'].mean()

# Step 10: Display the names of those who have done the DAP Course
dap_course_names = course_df[course_df['COURSE'] == 'DAP']['PNAME']

# Step 11: Display the lowest course fee
lowest_course_fee = courses_df['SCOST'].min()

# Step 12: Display the details of the packages for which development costs have been recovered
recovered_packages = courses_df[courses_df['SCOST'] >= courses_df['DCOST']]

# Step 13: What is the cost of the costliest software development in Basic
costliest_basic_dev = courses_df[courses_df['DEVELOPIN'] == 'BASIC']['DCOST'].max()

# Step 14: How many programmers paid 5000 to 10000 for their course
programmers_paid_range = len(courses_df[(courses_df['SCOST'] >= 5000) & (courses_df['SCOST'] <= 10000)])

# Step 15: How many programmers know either COBOL or Pascal
cobol_pascal_programmers = len(courses_df[courses_df['DEVELOPIN'].str.contains('COBOL|PASCAL', regex=True)])

# Display results
print("Average duration of each customer:\n", average_duration)
print("\nUnique transaction types:\n", unique_transaction_types)
print("\nCount of each transaction type with respect to each continent:\n", transaction_type_count)
print("\nAverage selling cost for Pascal packages:\n", pascal_avg_selling_cost)
print("\nNames of those who have done the DAP Course:\n", dap_course_names)
print("\nLowest course fee:\n", lowest_course_fee)
print("\nDetails of packages for which development costs have been recovered:\n", recovered_packages)
print("\nCost of the costliest software development in Basic:\n", costliest_basic_dev)
print("\nNumber of programmers who paid 5000 to 10000 for their course:\n", programmers_paid_range)
print("\nNumber of programmers who know either COBOL or Pascal:\n", cobol_pascal_programmers)
input()