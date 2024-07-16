import pandas as pd

# Read dataset
df = pd.read_csv('AIAAIC_corpus-10-2023.csv')

print("Head:")
print(df.head())

# Ensure column names have no extra spaces and are in the correct format
df.columns = df.columns.str.strip()

# Check column names
print("Columns: ", df.columns)

# Drop unnecessary columns
df = df.drop(columns=['Related link', 'ID'])

# Handle missing values in all string columns, converting them to empty strings
string_columns = ['AIAAIC Link', 'AIAAIC Article Title', 'Technology', 'Purpose', 'Issues', 'Country', 'Text']
for col in string_columns:
    df[col] = df[col].astype(str).fillna('')

# Function to clean and merge text
def clean_and_merge_text(texts):
    merged_text = ' '.join(texts)
    # Remove multiple spaces and newlines
    cleaned_text = ' '.join(merged_text.split())
    return cleaned_text

# Merge rows with the same AIAAIC Link
def merge_rows(group):
    merged_row = {
        'AIAAIC Link': group['AIAAIC Link'].iloc[0],
        'AIAAIC Article Title': ','.join(group['AIAAIC Article Title'].unique()),
        'Technology': ','.join(group['Technology'].unique()),
        'Purpose': ','.join(group['Purpose'].unique()),
        'Issues': ','.join(group['Issues'].unique()),
        'Country': ','.join(group['Country'].unique()),
        'Text': clean_and_merge_text(group['Text'])
    }
    return pd.Series(merged_row)

# Aggregate data
merged_df = df.groupby('AIAAIC Link').apply(merge_rows).reset_index(drop=True)

# Reset the ID column
merged_df.insert(0, 'ID', range(1, len(merged_df) + 1))

print("Processed Data Head:")
print(merged_df.head())

# Save the processed dataset
merged_df.to_csv('processed_data.csv', index=False)

print("Processed dataset has been successfully saved as processed_data.csv")
