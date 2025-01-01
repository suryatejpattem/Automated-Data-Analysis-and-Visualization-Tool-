# Automated Data Analysis and Visualization Tool

A Python-based tool to automate the process of data loading, exploratory data analysis (EDA), data cleaning, and visualization for CSV and Excel datasets.

---

## Features

- **Dynamic File Handling**: Supports loading of CSV and Excel files seamlessly.
- **Exploratory Data Analysis (EDA)**: Provides detailed summaries, including:
  - Data shape (rows and columns)
  - Missing values
  - Statistical insights for numerical and categorical data.
- **Data Cleaning**:
  - Handles missing values by filling them with mean (numerical columns) or mode (categorical columns).
  - Removes duplicates from datasets.
  - Converts date columns into proper datetime format where applicable.
- **Automated Visualizations**:
  - **Histograms**: For understanding the distribution of numerical data.
  - **Box Plots**: To detect outliers and visualize data spread.
  - **Bar Plots**: For categorical data insights.
  - **Pie Charts**: To visualize proportions in categorical data.
  - **Scatter Plots**: For relationships between numerical variables.
  - **Heatmaps**: To display correlations between numerical features.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - Pandas: For data manipulation and analysis
  - Matplotlib: For creating static visualizations
  - Seaborn: For advanced and aesthetically pleasing visualizations
  - Tabulate: For displaying tabular data in a readable format

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/Automated-Data-Analysis-and-Visualization-Tool.git


2. Install required libraries:

   ```bash
   pip install -r requirements.txt
3. Run the script:

   ```bash
   python automate.py
Provide the file path of the dataset when prompted and follow the instructions.

