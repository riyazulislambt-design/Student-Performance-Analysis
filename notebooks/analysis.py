
import pandas as pd

# Load dataset
df = pd.read_csv("../data/student.csv")

# 1. Total number of students
print("Total Students:", len(df))

# 2. Average marks of each subject
print("\nAverage Subject Marks:")
print(df[["Math", "English", "Science"]].mean())

# 3. Calculate total marks
df["Total_Marks"] = df[["Math", "English", "Science"]].sum(axis=1)

# 4. Calculate average marks
df["Average_Marks"] = df[["Math", "English", "Science"]].mean(axis=1)

# 5. Find top student
top_student = df.loc[df["Total_Marks"].idxmax()]

print("\nTop Student:")
print(top_student[["Name", "Total_Marks", "Average_Marks"]])

# 6. Gender distribution
print("\nGender Distribution:")
print(df["Gender"].value_counts())

# 7. Study hours and average marks
print("\nStudy Hours vs Average Marks:")
print(df[["Name", "Study_Hours", "Average_Marks"]])

# 8. Attendance and average marks
print("\nAttendance vs Average Marks:")
print(df[["Name", "Attendance", "Average_Marks"]])

# 9. Sort students by total marks
print("\nStudent Ranking:")
print(df[["Name", "Total_Marks"]].sort_values(
    by="Total_Marks", ascending=False
))

import matplotlib.pyplot as plt
import seaborn as sns

# Set chart style
sns.set_theme(style="whitegrid")

# 1. Subject Performance Bar Chart
subject_avg = df[["Math", "English", "Science"]].mean()

plt.figure(figsize=(8, 5))
subject_avg.plot(kind="bar")

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 2. Study Hours vs Average Marks
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Average_Marks",
    hue="Gender",
    s=100
)

plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()


# 3. Attendance Distribution
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Attendance",
    bins=5,
    kde=True
)

plt.title("Student Attendance Distribution")
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# ==================================
# DATA CLEANING
# ==================================

print("\n========== DATA CLEANING ==========")

# 1. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. Check data types
print("\nData Types:")
print(df.dtypes)

# 4. Check invalid marks
subjects = ["Math", "English", "Science"]

for subject in subjects:
    invalid = df[
        (df[subject] < 0) | (df[subject] > 100)
    ]

    print(f"\nInvalid {subject} Marks:")
    print(invalid[["Name", subject]])

# 5. Remove duplicate rows
df = df.drop_duplicates()

# 6. Handle missing values
for subject in subjects:
    df[subject] = df[subject].fillna(df[subject].mean())

# 7. Final dataset information
print("\nCleaned Dataset:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())

# ==================================
# CORRELATION ANALYSIS
# ==================================

print("\n========== CORRELATION ANALYSIS ==========")

# Select numerical columns
correlation_data = df[
    ["Study_Hours", "Attendance", "Math",
     "English", "Science", "Average_Marks"]
]

# Calculate correlation
correlation_matrix = correlation_data.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Correlation with Average Marks
print("\nCorrelation with Student Performance:")

performance_corr = correlation_matrix["Average_Marks"].sort_values(
    ascending=False
)

print(performance_corr)


# Visualize correlation using heatmap
plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Student Performance Correlation Heatmap")
plt.tight_layout()
plt.show()

# Compare independent factors with performance

factors = ["Study_Hours", "Attendance"]

factor_correlation = df[factors + ["Average_Marks"]].corr()

print("\nIndependent Factors Correlation:")
print(factor_correlation["Average_Marks"].drop("Average_Marks"))

# Identify the stronger association
strongest_factor = (
    factor_correlation["Average_Marks"]
    .drop("Average_Marks")
    .idxmax()
)

print("\nStrongest Associated Factor:", strongest_factor)

# ==========================================
# FINAL ANALYSIS REPORT & CSV EXPORT
# ==========================================

from pathlib import Path

# Create reports folder
reports_dir = Path("../reports")
reports_dir.mkdir(parents=True, exist_ok=True)

# Calculate important statistics
total_students = len(df)

subject_averages = df[
    ["Math", "English", "Science"]
].mean()

top_student = df.loc[df["Total_Marks"].idxmax()]

average_study_hours = df["Study_Hours"].mean()
average_attendance = df["Attendance"].mean()

# Calculate correlation
factor_corr = df[
    ["Study_Hours", "Attendance", "Average_Marks"]
].corr()

study_corr = factor_corr.loc[
    "Study_Hours", "Average_Marks"
]

attendance_corr = factor_corr.loc[
    "Attendance", "Average_Marks"
]

# Find strongest associated factor
strongest_factor = (
    factor_corr["Average_Marks"]
    .drop("Average_Marks")
    .idxmax()
)

# Generate report
report = f"""
========================================
      STUDENT PERFORMANCE ANALYSIS
========================================

1. DATASET OVERVIEW
-------------------
Total Students: {total_students}

Average Study Hours: {average_study_hours:.2f}
Average Attendance: {average_attendance:.2f}%

2. SUBJECT PERFORMANCE
----------------------
Math Average: {subject_averages['Math']:.2f}
English Average: {subject_averages['English']:.2f}
Science Average: {subject_averages['Science']:.2f}

3. TOP PERFORMER
----------------
Name: {top_student['Name']}
Total Marks: {top_student['Total_Marks']}
Average Marks: {top_student['Average_Marks']:.2f}

4. CORRELATION ANALYSIS
-----------------------
Study Hours vs Average Marks: {study_corr:.2f}
Attendance vs Average Marks: {attendance_corr:.2f}

Strongest Associated Factor: {strongest_factor}

5. KEY FINDINGS
---------------
- English has the highest average subject marks.
- {top_student['Name']} achieved the highest total marks.
- Attendance has a stronger positive correlation
  with Average Marks than Study Hours in this sample.

6. CONCLUSION
-------------
The sample dataset shows positive associations between
study hours, attendance and student performance.

Correlation does not prove causation.
The dataset contains only 10 sample students,
so the findings should not be generalized.

========================================
             END OF REPORT
========================================
"""

# Save report
report_path = reports_dir / "analysis_report.txt"
report_path.write_text(report, encoding="utf-8")

# Export cleaned dataset
csv_path = reports_dir / "cleaned_student_data.csv"
df.to_csv(csv_path, index=False)

print("\n========== FINAL REPORT ==========")
print(report)

print("Report saved:", report_path)
print("Cleaned CSV saved:", csv_path)
