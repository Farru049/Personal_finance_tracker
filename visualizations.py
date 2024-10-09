import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to create a pie chart for expense categories
def pie_chart(expenses):
    category_counts = expenses['Category'].value_counts()
    
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, 
                                        textprops={'fontsize': 10}, wedgeprops={'linewidth': 1, 'edgecolor': 'black'})
    
    # Set the legend to avoid overlap
    plt.legend(wedges, category_counts.index, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

    plt.title('Expenses by Category')
    output_file = os.path.join('static/visualizations', 'pie_chart.png')
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.savefig(output_file)
    plt.close()
    return output_file

# Function to create a bar chart for monthly expenses
def bar_chart(expenses):
    monthly_expenses = expenses.groupby('Month')['Amount'].sum()
    plt.figure(figsize=(10, 6))
    monthly_expenses.plot(kind='bar', color='skyblue')
    plt.title('Monthly Expenses')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout
    output_file = os.path.join('static/visualizations', 'bar_chart.png')
    plt.savefig(output_file)
    plt.close()
    return output_file

# Function to create a line chart for expenses over time
def line_chart(expenses):
    monthly_expenses = expenses.groupby('Month')['Amount'].sum()
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_expenses.index, monthly_expenses, marker='o', linestyle='-', color='purple')
    plt.title('Expenses Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout
    output_file = os.path.join('static/visualizations', 'line_chart.png')
    plt.savefig(output_file)
    plt.close()
    return output_file

# Function to create a histogram of expenses
def histogram(expenses):
    plt.figure(figsize=(10, 6))
    sns.histplot(expenses['Amount'], bins=10, kde=True, color='teal')
    plt.title('Distribution of Expenses')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.tight_layout()  # Adjust layout
    output_file = os.path.join('static/visualizations', 'histogram.png')
    plt.savefig(output_file)
    plt.close()
    return output_file

# Function to generate all visualizations
def generate_visualizations(expenses):
    pie_chart_path = pie_chart(expenses)
    bar_chart_path = bar_chart(expenses)
    line_chart_path = line_chart(expenses)
    histogram_path = histogram(expenses)
    return pie_chart_path, bar_chart_path, line_chart_path, histogram_path
