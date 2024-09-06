TV Advertising Budget vs Sales Analysis
Overview
This script analyzes the relationship between TV advertising budgets and sales using a scatter
plot. It visualizes how changes in TV advertising expenditure impact sales.
Requirements
To run this code, you need the following Python libraries:
 pandas
 matplotlib
You can install these libraries using pip:
bash
Copy code
pip install pandas matplotlib
Data
The script uses a dataset named Advertising.csv, which should be located in the same
directory as the script. This dataset contains the following columns:
 TV: Budget allocated to TV advertising.
 Sales: Sales figures.
Script Breakdown
1. Data Loading:
o The dataset is loaded into a pandas DataFrame.
o Basic information about the dataset is displayed using df.info().
2. Data Preview:
o A new DataFrame df_new is created by selecting the first 7 rows of the dataset.
o The contents of this new DataFrame are printed to verify the selection.
3. Scatter Plot:
o A scatter plot is created to visualize the relationship between TV and Sales.
o Axis labels and a title are added for clarity.
4. Full Dataset Plotting:
o An additional plot is generated to visualize all data points.

Running the Script
To run the script, execute the following command in your terminal:
bash
Copy code
python tv_advertising_analysis.py
Make sure to replace tv_advertising_analysis.py with the actual filename of your script.
Results
 The script generates scatter plots showing how TV advertising budgets relate to sales
figures.
 The first plot shows the relationship for a subset of 7 rows, while the second plot
visualizes all data points.
