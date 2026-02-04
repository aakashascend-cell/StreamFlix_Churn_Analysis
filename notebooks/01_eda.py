import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import math

def data_load(data_loc):
    data_df = pd.read_csv(data_loc)
    return data_df

def basic_data_info(data_to_exp):
    #Display basic information about the dataset
    print(base_data.info())

    # Display the first few rows of the dataset
    print(base_data.head().T)

    #Total Customers
    print("Total Customers:", base_data['customerID'].nunique())

def data_visualizations_bar(data_to_visual,chart_label):
    
    ax = sns.barplot(x=data_to_visual.index, y=data_to_visual.values, palette='viridis')
    
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width()/2., height + 50,
                f'{int(height):,}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
        
    plt.xlabel(chart_label)
    plt.ylabel('# of customers')
    plt.title(f' Customer distribution by {chart_label}', wrap=True)
    
if __name__ == "__main__":
    raw_data_loc = '/Users/hypernova/Public/Akash Stuff/Stream_Flix/StreamFlix_Churn_Analysis/data/raw/Customer-Churn.csv'
    # get the data
    base_data = data_load(raw_data_loc)
    
    # basic data exploration
    #basic_data_info(base_data)
    base_data['SeniorCitizen'] = base_data['SeniorCitizen'].replace({0:'No',1:'Yes'})
    base_data = base_data[base_data['TotalCharges']!= ' ']
    base_data['TotalCharges'] = pd.to_numeric(base_data['TotalCharges'])
    
    # basic data visualization
    #data_visualizations(base_data)
    column_to_analyse = [col for col in base_data.columns if base_data[col].dtype == 'object' and col != 'customerID']
    #print(column_to_analyse)
    
    tot_col = len(column_to_analyse)

    cols = 4

    rows = math.ceil(tot_col/cols)

    i = 1
    
    plt.figure(figsize=(15,4*rows))
    
    for col in column_to_analyse:
        var_data = base_data[col].value_counts()

        plt.subplot(rows,cols,i)
        data_visualizations_bar(var_data,col)
        i +=1
        
    plt.tight_layout()
    plt.show()





