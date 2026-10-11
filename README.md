# Retail Sales Data Analyzer

### Description

The **Retail Sales Data Analyzer** is a Python-based project that analyzes retail sales data stored in a CSV file. It allows users to load and clean data, calculate important sales metrics, filter records, display summary reports, and visualize sales information using different graphs.

The project uses NumPy and Pandas for data analysis, Matplotlib for creating charts, and Seaborn for generating a correlation heatmap.

### Features

- Loads retail sales data from a CSV file.
- Displays the first five rows of the dataset.
- Checks for required columns in the dataset.
- Cleans data by identifying and removing invalid records.
- Removes duplicate records.
- Calculates total sales using price and quantity sold.
- Calculates total, average, highest, and lowest sales.
- Identifies the most popular product based on quantity sold.
- Displays sales by category.
- Calculates sales growth between the latest two dates when possible.
- Filters sales data using user-defined conditions.
- Generates a summary report of the dataset.
- Creates a bar chart for sales by category.
- Creates a line graph to display sales trends over time.
- Creates a heatmap showing the correlation between price and quantity sold.
- Displays dataset dimensions, column names, data types, and non-null values.
- Provides a menu-driven interface for easy interaction.

### Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- `read_csv()`
- `head()`
- `to_datetime()`
- `to_numeric()`
- `groupby()`
- `query()`
- `dropna()`
- `drop_duplicates()`
- `mean()`
- `sum()`
- `max()`
- `min()`
- `type()`
- Exception handling
- Object-Oriented Programming (OOP)

### Dataset Requirements

The CSV file must contain the following columns:

- Date
- Product
- Category
- Price
- Quantity Sold
- Total Sales

The program recalculates Total Sales using the formula:

**Total Sales = Price × Quantity Sold**

### How to Run

1. Install Python 3.10 or later.
2. Install the required libraries:

   ```bash
   pip install numpy pandas matplotlib seaborn
   ```

3. Save the Python code as `retail_analyzer.py`.
4. Run the program:

   ```bash
   python retail_analyzer.py
   ```

5. Select an option from the main menu.
6. Load the CSV file and clean the data before performing analysis.
7. Select option 8 to exit the program.
### Main Menu

1. Load Data
2. Clean Data
3. Calculate Sales Metrics
4. Filter Data
5. Display Summary Report
6. Visualize Data
7. Display Dataset Information
8. Exit

### Project Structure

```text
practical_test/
├── final_project/
      ├── retail_analyzer.py
      ├── retail_sales.csv
├── README.md
```

**Created by:** Hetvi Patel
