# Test Task Python

This program uses the iris dataset, takes the output file name and the format, as input parameters and generates a summary of statistics for each column in the dataset. 


## Features

- Computes detailed statistical metrics for each column in the dataset:
  - Data type
  - Minimum and maximum values
  - Mean, median, and mode
  - Percentage of missing values (`zero_rows_pr`)
  - Variance and standard deviation
  - Interquartile range
  - Coefficient of variation
  - Number of distinct values
- Input options for the output  format:
  - **excel - for Excel (.xlsx)**
  - **markdown - for Markdown (.md)**
  - **html - for HTML**

---

## How to run

Create and activate a virtual environment
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

Install the required libraries using:

```bash
pip install -r requirements.txt
```
Run the script
```bash
python3 main.py
```