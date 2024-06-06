import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data from Excel file
excel_file = "nba1.xlsx"
df = pd.read_excel(excel_file)

# Define your dashboard functions
def plot_bar_chart(df, column, ax):
    sns.countplot(data=df, x=column, color='#1a81aa', edgecolor='Black', ax=ax)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    ax.tick_params(rotation=45)
    ax.set_facecolor('#0000FF')  # Set background color

def plot_histogram(df, column, ax):
    sns.histplot(data=df, x=column, bins=20, kde=True, ax=ax)
    ax.set_title(f"Histogram of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.set_facecolor('#0000FF')  # Set background color

def plot_boxplot(df, x_column, y_column, ax):
    sns.boxplot(data=df, x=x_column, y=y_column, ax=ax)
    ax.set_title(f"Boxplot of {y_column} by {x_column}")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.tick_params(rotation=45)
    ax.set_facecolor('#0000FF')  # Set background color

def plot_pie_chart(df, column, ax):
    data = df[column].value_counts()
    ax.pie(data, labels=data.index, startangle=140)
    ax.set_title(f"Pie Chart of {column}")
    ax.set_facecolor('#0000FF')  # Set background color

def plot_stacked_bar_chart(df, column1, column2, ax):
    data = df[[column1, column2]].groupby(column1)[column2].sum()
    data.plot(kind='bar', stacked=True, ax=ax, color=['#1a81aa', '#FF4500'], edgecolor='Black')
    ax.set_title(f"Stacked Bar Chart of {column1} and {column2}")
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.tick_params(rotation=45)
    ax.set_facecolor('#f0f0f0')  # Set background color


def plot_doughnut_chart(df, column, ax):
    data = df[column].value_counts()
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
    ax.set_title(f"Doughnut Chart of {column}")
    ax.set_aspect('equal')
    ax.set_facecolor('#f0f0f0')  # Set background color

def filter_data(df):
    print("Filter Options:")
    print("1. Filter by Team")
    print("2. Filter by Position")
    print("3. No Filter")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        team = input("Enter team name: ")
        df = df[df['Team'] == team]
    elif choice == "2":
        position = input("Enter position: ")
        df = df[df['Position'] == position]
    elif choice == "3":
        pass  # No filter, use the original DataFrame
    else:
        print("Invalid choice. Applying no filter.")
    return df

# Create a figure and subplots
fig, axes = plt.subplots(3, 2, figsize=(15, 10))



# Example dashboard
while True:
    print("Dashboard Options:")
    print("1. Plot Bar Chart")
    print("2. Plot Histogram")
    print("3. Plot Boxplot")
    print("4. Plot Pie Chart")
    print("5. Plot Stacked Bar Chart")
    print("6. Plot Doughnut Chart")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        column = input("Enter column name to plot bar chart: ")
        plot_bar_chart(df, column, axes[0, 0])
    elif choice == "2":
        column = input("Enter column name to plot histogram: ")
        plot_histogram(df, column, axes[0, 1])
    elif choice == "3":
        x_column = input("Enter x-axis column name: ")
        y_column = input("Enter y-axis column name: ")
        plot_boxplot(df, x_column, y_column, axes[1, 0])
    elif choice == "4":
        column = input("Enter column name to plot pie chart: ")
        plot_pie_chart(df, column, axes[1, 1])
    elif choice == "5":
        column1 = input("Enter column name for stacking (x-axis): ")
        column2 = input("Enter column name for stacking (y-axis): ")
        plot_stacked_bar_chart(df, column1, column2, axes[0, 0])
    elif choice == "6":
        column = input("Enter column name to plot doughnut chart: ")
        plot_doughnut_chart(df, column, axes[0, 1])
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

# Adjust layout and show plot
plt.tight_layout()
plt.show()
