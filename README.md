
# Student Performance Analysis

## Project Overview

This project analyzes student academic performance using Python and Data Science libraries.

The main objective is to explore student performance and understand the relationship between study hours, attendance, and academic results.

## Dataset Information

The dataset contains 10 sample student records with the following features:

- Student ID
- Name
- Gender
- Study Hours
- Attendance
- Math Marks
- English Marks
- Science Marks

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Project Workflow

1. Data Collection
2. CSV Data Loading
3. Data Exploration
4. Statistical Analysis
5. Data Cleaning
6. Student Ranking
7. Correlation Analysis
8. Data Visualization
9. Final Report Generation

## Key Findings

- English has the highest average marks.
- Ayesha achieved the highest total marks (283).
- Attendance has a stronger positive correlation with average marks than study hours in this sample.
- The dataset contains no missing values or duplicate rows.

## Project Structure

```text
Student-Performance-Analysis/
│
├── data/
│   └── student.csv
│
├── notebooks/
│   └── analysis.py
│
├── reports/
│   ├── analysis_report.txt
│   └── cleaned_student_data.csv
│
└── README.md
```

## How to Run

### 1. Install Required Libraries

```bash
py -m pip install numpy pandas matplotlib seaborn scikit-learn
```

### 2. Navigate to the Project

```bash
cd Student-Performance-Analysis/notebooks
```

### 3. Run the Analysis

```bash
py analysis.py
```

## Important Note

This project uses a small sample dataset of 10 students for educational purposes.

The correlation results indicate associations, not causation. These findings should not be generalized to real-world student populations.

## Author

Riyazul Islam
