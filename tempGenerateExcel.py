import pandas as pd
import numpy as np

# Define the date range (Sep 1 to Oct 31, 2025)
start_date = '2025-09-01'
end_date = '2025-10-31'
date_range = pd.date_range(start=start_date, end=end_date)
all_dates = date_range.strftime('%Y-%m-%d').to_numpy()

# Randomly sample 1287 dates WITH replacement (to allow repeats/missing dates)
num_samples = 1287
np.random.seed(42) # Set a seed for reproducibility if you want the *exact* same list
random_dates = np.random.choice(all_dates, size=num_samples, replace=True)

# Create the DataFrame
df = pd.DataFrame(random_dates, columns=['RandomDate'])

# Save the DataFrame to a CSV file in your current directory
df.to_csv('random_dates_1287.csv', index=False)

print("Successfully generated and saved 'random_dates_1287.csv' with 1287 rows.")
print("The file is located in the directory where you ran this code.")