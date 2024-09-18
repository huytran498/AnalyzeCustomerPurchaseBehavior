import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
df = pd.read_csv('CustomerPurchasingBehaviors.csv')

# Data Cleaning
print("Original data shape:", df.shape)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")
df.drop_duplicates(inplace=True)

# Check for outliers using IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

numeric_columns = ['age', 'annual_income', 'purchase_amount', 'loyalty_score', 'purchase_frequency']
for col in numeric_columns:
    df = remove_outliers(df, col)

print("Data shape after cleaning:", df.shape)

# Data Exploration
print("\nBasic statistics:")
print(df.describe())

print("\nData types:")
print(df.dtypes)

print("\nUnique values in 'region':")
print(df['region'].unique())

# Correlation matrix
correlation = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Customer Purchasing Behaviors')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.close()

# Distribution plots for numeric variables
fig, axes = plt.subplots(3, 2, figsize=(15, 20))
fig.suptitle('Distribution of Numeric Variables', fontsize=16)

for i, col in enumerate(numeric_columns):
    sns.histplot(df[col], kde=True, ax=axes[i//2, i%2])
    axes[i//2, i%2].set_title(f'Distribution of {col}')
    if col == 'age':
        axes[i//2, i%2].set_xticks(np.arange(df[col].min(), df[col].max()+1, 5))

plt.tight_layout()
plt.savefig('numeric_distributions.png')
plt.close()

# Boxplot of purchase amount by region
plt.figure(figsize=(10, 6))
sns.boxplot(x='region', y='purchase_amount', data=df)
plt.title('Purchase Amount Distribution by Region')
plt.savefig('purchase_amount_by_region.png')
plt.close()

# Age groups and their average purchase amounts
df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 45, 55, 100], labels=['18-25', '26-35', '36-45', '46-55', '55+'])
avg_purchase_by_age = df.groupby('age_group')['purchase_amount'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
avg_purchase_by_age.plot(kind='bar')
plt.title('Average Purchase Amount by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Purchase Amount')
plt.savefig('avg_purchase_by_age.png')
plt.close()

# Correlation between loyalty score and other variables
loyalty_correlation = df[['loyalty_score', 'age', 'annual_income', 'purchase_amount', 'purchase_frequency']].corr()['loyalty_score'].sort_values(ascending=False)
print("\nCorrelation with loyalty score:")
print(loyalty_correlation)

# Average metrics by region
region_metrics = df.groupby('region').agg({
    'age': 'mean',
    'annual_income': 'mean',
    'purchase_amount': 'mean',
    'loyalty_score': 'mean',
    'purchase_frequency': 'mean'
}).round(2)

print("\nAverage metrics by region:")
print(region_metrics)

# Top 10 customers by purchase amount
top_customers = df.nlargest(10, 'purchase_amount')[['user_id', 'purchase_amount']]
print("\nTop 10 customers by purchase amount:")
print(top_customers)

print("\nAnalysis complete. Check the generated PNG files for visualizations.")