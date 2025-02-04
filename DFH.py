import pandas as pd
import numpy as np

employee_data = {
    "Name": ["Abdullah", "Aroosh", "Hasnain", "Umair"],
    "Role": ["CEO", np.nan, np.nan, np.nan],
    "Salary": [100, 200, np.nan, np.nan]
}

Labels = ["a", "b", "c", "d"]

df = pd.DataFrame(employee_data, index=Labels)

print("Summary of the basic information about this DataFrame and its data:")
print(df)

df = df.assign(
    Role=df["Role"].fillna("Unknown"),
    Salary=df["Salary"].fillna(0)
)

print("\nUpdated DataFrame after handling missing values:")
print(df)