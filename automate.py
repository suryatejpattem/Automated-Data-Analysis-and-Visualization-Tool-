import pandas as pd
import string
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate


#-----Loading the dataset-----#
def load_dataset(file_path):
    try:
        if file_path.endswith(".csv"):
            data=pd.read_csv(file_path,encoding='ISO-8859-1')
        elif file_path.endswith(".xls",".xlsx"):
            data=pd.read_excel(file_path,encoding='ISO-8859-1')
        else:
            print("Inavlid file")
            exit()
        print("Dataset successfully Loaded!\n")
        return data
    except FileNotFoundError:
        print("Error: Unsupported file format")
        return None
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
    
#-----Exploratory Data Analysis-----#
def EDA(data):
    try:
        eda_summary={
            "Shape(Rows & columns)":data.shape,
            "Columns names":data.columns.tolist(),
            "Datatypes":data.dtypes.to_dict(),
            "Missing values":data.isnull().sum().to_dict()
        }
        numerical_summary=data.describe(include=[float,int])
        categorical_summary=data.describe(include=object)

        eda_summary["numerical summary"]=numerical_summary
        eda_summary["categorical summary"]=categorical_summary
        
        print("Exploratory data analysis is completed successfully!\n")
        print(tabulate(eda_summary.items(), headers=["EDA Component", "Details"], tablefmt="grid"))
        return eda_summary
    
    except Exception as e:
        print(f"Error during EDA:{e}")
        return None

   
#-----Data cleaning-----#
def data_cleaning(data):
    try:

        #checking the missing values
        missing_threshold=50
        missing_percent=data.isnull().sum()/len(data)*100
        cols_to_drop=missing_percent[missing_percent>missing_threshold].index
        data=data.drop(columns=cols_to_drop)
        if cols_to_drop is not None:
            print(f"Columns with more than {missing_threshold}% missing percent are dropped\n")
            print(f"dropped columns are : {list(cols_to_drop)}" )
        else:
            print("no columns are dropped")

        for col in data.select_dtypes(include=['float64','int64']).columns:
            if data[col].isnull().sum()>0:
                data[col]=data[col].fillna(data[col].mean())
                print(f"Filled missing values with mean for numerical column {col}")
        print("\n")
        for col in data.select_dtypes(include='object').columns:
            if data[col].isnull().sum()>0:
                data[col]=data[col].fillna(data[col].mode()[0])
                print(f"Filled missing values with mode for categorical column {col}")

        before_dupliates=data.shape[0]
        data=data.drop_duplicates()
        after_duplicates=data.shape[0]
        print("\n")
        print(f"Removed {before_dupliates-after_duplicates} duplicates")
        print("\n")
        for col in data.select_dtypes(include=['object']).columns:
            try:
                data[col] = pd.to_datetime(data[col],format="%Y-%m-%d")
                print(f"Converted column '{col}' to datetime.")
            except Exception as e:
                print(f"Could not convert '{col}' to datetime format. Skipping... ")


        print("Data cleaning is completed sucessfully")
        return data
    
    except Exception as e:
        print("Error during data cleaning")
        return None




#-----Data visualization-----#

def visualize_data(data):
    try:
        # Set up the plot style
        sns.set(style="whitegrid")
        
        # 1. Histogram for numerical columns 
        numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
        for col in numerical_cols:
            plt.figure(figsize=(10, 6))  # Adjust figure size
            sns.histplot(data[col], kde=True)
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.tight_layout()  # Ensure proper layout
            plt.show()
        
        #2.Box plot for numerical columns
        numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
        for col in numerical_cols:
            plt.figure(figsize=(10, 6))  # Adjust figure size
            sns.boxplot(x=data[col])
            plt.title(f"Box Plot of {col}")
            plt.xlabel(col)
            plt.tight_layout()  # Ensure proper layout
            plt.show()



        # 3. Bar Graph and Pie Chart for categorical columns
        categorical_cols = data.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            # Count occurrences of categories
            count_data = data[col].value_counts()
            
            # Limit to top N categories if there are too many
            if len(count_data) > 20:
                count_data = count_data.head(20)
            
            # 3a. Bar Plot
            plt.figure(figsize=(12, 8))  # Adjust figure size
            sns.barplot(x=count_data.index, y=count_data.values)
            plt.title(f"Bar Plot of {col}")
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()  # Ensure proper layout
            plt.show()

            # 3b. Pie Chart
            plt.figure(figsize=(12, 8))
            count_data.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(count_data)))
            plt.title(f"Pie Chart of {col}")
            plt.ylabel('')  # Hide the y-label for better aesthetics
            plt.tight_layout()
            plt.show()

        # 4. Pairplot for numerical variables 
        if len(numerical_cols) > 1:
            plt.figure(figsize=(10, 8))
            sns.pairplot(data[numerical_cols])
            plt.suptitle("Pairplot of Numerical Columns", y=1.02)
            plt.show()

        # 5. Scatter plot for numerical data
        if len(numerical_cols) > 1:
            for i in range(len(numerical_cols)):
                for j in range(i + 1, len(numerical_cols)):
                    plt.figure(figsize=(10, 6))
                    sns.scatterplot(x=data[numerical_cols[i]], y=data[numerical_cols[j]])
                    plt.title(f"Scatter Plot of {numerical_cols[i]} vs {numerical_cols[j]}")
                    plt.xlabel(numerical_cols[i])
                    plt.ylabel(numerical_cols[j])
                    plt.tight_layout()  # Ensure proper layout
                    plt.show()

        # 6. Heat map for numerical columns
        numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
        correlation_matrix = data[numerical_cols].corr()
        plt.figure(figsize=(12, 8))  # Adjust figure size
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.tight_layout()  # Ensure proper layout
        plt.show()

        print("Visualizations completed successfully!")
        
    except Exception as e:
        print(f"Error during data visualization: {e}")



#main
def main():
    file_path=input("Enter the file path:")
    df=load_dataset(file_path)
    if df is not None:
        print(df.head(5))
        eda_results=EDA(df)
        if eda_results is not None:
            for items in eda_results.items():
                print(items)
        cleaned_data=data_cleaning(df)
        if cleaned_data is not None:
            print(cleaned_data.head())
        if cleaned_data is not None:
            visualize_data(cleaned_data)


if __name__=="__main__":
    main()
    
