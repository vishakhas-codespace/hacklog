import pandas as pd
import numpy as np

# ─── PART A: Dataset Creation ───────────────────────────────────────────────

data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name':        ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Department':  ['IT', 'Finance', 'IT', 'HR', 'HR'],
    'Days_Present': [24, 22, 23, 21, 18],
    'Total_Days':   [26, 26, 26, 26, 26],
    'Leaves_Taken': [2, 4, 3, 5, 8],
    'Working_Hours': [190, 175, 185, 168, 140],
    'Tasks_Completed': [25, 16, 22, 16, 14]
}

df = pd.DataFrame(data)
print("=== Dataset Head ===")
print(df.head())

# ─── PART B: Data Preprocessing ─────────────────────────────────────────────

print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Duplicate Rows ===")
df = df.drop_duplicates()
print("Duplicate rows after removal:", df.duplicated().sum())

print("\n=== Statistical Summary ===")
print(df.describe())

# ─── PART C: Data Analysis ───────────────────────────────────────────────────

df['Attendance_%'] = (df['Days_Present'] / df['Total_Days']) * 100

print("\n=== Attendance Percentage ===")
print(df[['Employee_ID', 'Name', 'Attendance_%']])

avg_hours = df['Working_Hours'].mean()
print(f"\nAverage Working Hours: {avg_hours}")

dept_tasks = df.groupby('Department')['Tasks_Completed'].mean()
print("\n=== Department-wise Avg Tasks ===")
print(dept_tasks)
