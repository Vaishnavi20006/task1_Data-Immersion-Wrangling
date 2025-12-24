import pandas as pd

# Read data
data = pd.read_csv("data.csv")

# Show first rows
print("Original Data:")
print(data)

# Remove missing values
data = data.dropna()

# Remove duplicates
data = data.drop_duplicates()

# Save cleaned data
data.to_csv("cleaned_data.csv", index=False)

print("Cleaned data saved successfully!")
