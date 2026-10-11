# Import libraries required for data analysis and visualization
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Create a class to analyze retail sales data
class RetailAnalyzer:

    # Initialize the DataFrame as empty
    def __init__(self):
        self.df = None

    # Load sales data from a CSV file and check required columns
    def load_data(self,file_path):
        required_columns = ["Date", "Product", "Category","Price", "Quantity Sold", "Total Sales"]
        try:
            data = pd.read_csv(file_path)
            for column in required_columns:
                if column not in data.columns:
                    raise ValueError("Missing column: " + column)
            self.df =data
            print("Data loaded successfully!")
            print("print top 5 line of dataset")
            print(self.df.head(5))
        except FileNotFoundError:
            print("Error : File not found. check the file path")
        except pd.errors.EmptyDataError:
            print("Error: File is empty.")
        except ValueError as e:
            print("Error:",e)

    # Check whether data is loaded and contains records
    def check_data(self):
        if self.df is None:
            print("Please load the CSV file first.")
            return False
        if self.df.empty:
            print("No data available.")
            return False
        return True
    
    # Clean data by removing invalid records and duplicates
    def clean_data(self):
        if self.df is None:
            print("Please load data first.")
            return
        try:
            original_count = len(self.df)

            self.df["Date"] = pd.to_datetime(self.df["Date"])
            for column in ["Price", "Quantity Sold"]:
                self.df[column] = pd.to_numeric(self.df[column])
            invalid_count = 0
            for index, row in self.df.iterrows():
                invalid = False
                if pd.isna(row["Date"]):
                    invalid = True
                elif pd.isna(row["Product"]):
                    invalid = True
                elif pd.isna(row["Category"]):
                    invalid = True
                elif pd.isna(row["Price"]):
                    invalid = True
                elif pd.isna(row["Quantity Sold"]):
                    invalid = True
                elif row["Price"] < 0:
                    invalid = True
                elif row["Quantity Sold"] < 0:
                    invalid = True
                if invalid:
                    invalid_count += 1
            self.df.dropna(subset=["Date", "Product", "Category","Price", "Quantity Sold"],inplace=True)

            self.df = self.df[(self.df["Price"] >= 0)& (self.df["Quantity Sold"] >= 0)]

            price_array = np.array(self.df["Price"])

            quantity_array = np.array(self.df["Quantity Sold"])

            self.df["Total Sales"] = price_array * quantity_array

            self.df.drop_duplicates(inplace=True)

            self.df.reset_index(drop=True, inplace=True)

            print("\nData cleaning completed!")
            print("Original records:", original_count)
            print("Invalid records identified:", invalid_count)
            print("Remaining records:", len(self.df))
            print("Records removed:", original_count - len(self.df))
        except (ValueError,TypeError) as e:
            print("Error: Invalid data value in the CSV.")
            print(e)
            return
        
    # Calculate sales metrics
    def calculate_metrics(self):
        if self.df is None:
            print("Please load data")
            return
        if self.df.empty:
            print("No data available.")
            return
        total_sales = np.sum(self.df["Total Sales"])
        print("Total Sales:",total_sales)

        print("------------------------------------------------------------")
        avg_sales = np.mean(self.df["Total Sales"])
        print("Average Sales:",avg_sales)

        print("------------------------------------------------------------")
        high_sale = np.max(self.df["Total Sales"])
        print("Highest Sales:",high_sale)

        print("------------------------------------------------------------")
        low_sale = np.min(self.df["Total Sales"])
        print("Lowest Sales:",low_sale)

        print("------------------------------------------------------------")
        popular_product = self.df.groupby("Product")["Quantity Sold"].sum().sort_values(ascending=False)
        print("Most popular product:",popular_product.index[0])

        print("------------------------------------------------------------")
        category_sales = self.df.groupby("Category")["Total Sales"].sum()
        print("Sales by Category:")
        print(category_sales)

        print("------------------------------------------------------------")
        daily_sales = (self.df.groupby("Date")["Total Sales"].sum().sort_index())
        if len(daily_sales) >= 2:
            previous_sales = daily_sales.iloc[-2]
            current_sales = daily_sales.iloc[-1]
            if previous_sales != 0:
                growth = np.divide(current_sales - previous_sales,previous_sales) * 100
                print("Sales Growth:", round(growth, 2), "%")
            else:
                print("Growth unavailable: previous sales are zero.")
        else:
            print("Not enough dates to calculate growth.")

    # Filter sales data
    def filter_data(self,condition):
        if self.df is None:
            print("Please load data")
            return
        try:
            filtered_data = self.df.query(condition)
            print(filtered_data)
        except (ValueError,SyntaxError,TypeError,KeyError,NameError) as e:
            print("Error:Invalid filter condition.")
            print(e)

    # Display a summary report of the retail sales data
    def display_summary(self):
        if self.df is None:
            print("Please load data")
            return
        if self.df.empty:
            print("No data available.")
            return
        print("------------------------------------------------------------")
        print("----------------Retail sales summary report----------------")
        print("------------------------------------------------------------")
        print("Total Sales:",self.df["Total Sales"].sum())
        print()
        print("Average Sales:",self.df["Total Sales"].mean())
        print()
        print("Total Quantity Sold:",self.df["Quantity Sold"].sum())
        print()
        print("Total Products:",len(self.df["Product"].drop_duplicates()))
        print()
        print("Total Categories:",len(self.df["Category"].drop_duplicates()))
        print()
        print("Total Records:",len(self.df))
        print()
        popular_product = self.df.groupby("Product")["Quantity Sold"].sum().sort_values(ascending=False)
        print("Most popular product:",popular_product.index[0])
        print()
        print("Sales by Category:")
        print(self.df.groupby("Category")["Total Sales"].sum())

    # Display a menu of graphs for visualizing sales data
    def visualize_data(self):
        if self.df is None:
            print("Please load data")
            return
        if not self.check_data():
            return
        while True:
            print("1.Bar chart - Sales by Category")
            print("2.Line Graph - Sales Trend")
            print("3.Heatmap - Price and Quantity Correlation")
            print("4.Back to main menu")
            try:
                choice = int(input("Enter your choice:"))
                match choice:
                    case 1:
                        category_sales = self.df.groupby("Category")["Total Sales"].sum()
                        category_sales.plot(kind="bar",color ="yellow",edgecolor = "black")
                        plt.title("Total Sales by Category")
                        plt.xlabel("Product Category")
                        plt.ylabel("Total Sales")
                        plt.legend()
                        plt.grid()
                        plt.ticklabel_format(axis="y",style="plain")
                        plt.ticklabel_format(axis="y",useOffset=False)
                        plt.tight_layout()
                        plt.show()
                    case 2:
                        daily_sales = self.df.groupby("Date")["Total Sales"].sum().sort_index()
                        daily_sales.plot(kind="line",marker = "o",color = "skyblue")
                        plt.title("Sales Trend Over Time")
                        plt.xlabel("Date")
                        plt.ylabel("Total Sales")
                        plt.xticks(rotation = 45)
                        plt.legend()
                        plt.grid()
                        plt.tight_layout()
                        plt.show()
                    case 3:
                        correlation = self.df[["Price","Quantity Sold"]].corr()
                        sns.heatmap(correlation,annot=True,cmap="coolwarm",vmin=-1,vmax=1,center=0,linewidths=1,square=True,fmt=".2f")
                        plt.title("Price and Quantity Correlation")
                        plt.tight_layout()
                        plt.show()
                    case 4:
                        break
                    case _:
                        print("Invalid choice!")
            except ValueError:
                print("Error: Please enter a number from 1 to 4")

    # Display dataset dimensions, column names, and data types
    def display_info(self):
        if not self.check_data():
            return
        print("--------------- DATASET INFORMATION ---------------")
        print("Rows and Columns:", self.df.shape)
        print("Column Names:", list(self.df.columns))
        print("Data Types and Non-null Values:")
        self.df.info()

    # Display the main menu and execute the selected operation
    def main(self):
        print("Welcome to Retail Sales Data Analyzer ")

        while True:
            print("------------------------------------------------------------------------")
            print("1.Load Data")
            print("2.Clean Data")
            print("3.Calculate Sales Metrics")
            print("4.Filter Data")
            print("5.Display Summary Report")
            print("6.Visualize Data")
            print("7.Display Dataset Information")
            print("8.Exit")
            print("------------------------------------------------------------------------")
            try:
                choice = int(input("Enter your choice:"))
                match choice:
                    case 1:
                        file_path = input("Enter CSV file path:")
                        self.load_data(file_path)
                        print()
                    case 2:
                        self.clean_data()
                        print()
                    case 3:
                        self.calculate_metrics()
                        print()
                    case 4:
                        condition = input("Enter condition to filter data:")
                        self.filter_data(condition)
                        print("")
                        print()
                    case 5:
                        self.display_summary()
                        print()
                    case 6:
                        self.visualize_data()
                        print()
                    case 7:
                        self.display_info()
                        print()
                    case 8:
                        print("-------------------------------------------------------------")
                        print("Thank you for using Retail Sales Data Analyzer!")
                        print("--------------------------------------------------------------")
                        break
                    case _:
                        print("Invalid choice")
            except ValueError:
                print("Error: Please enter a number from 1 to 8.")

if __name__ == "__main__":
    analyzer = RetailAnalyzer()
    analyzer.main()