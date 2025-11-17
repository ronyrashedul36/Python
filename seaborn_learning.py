import seaborn as sns

import matplotlib.pyplot as plt

import pandas as pd

tips = sns.load_dataset('tips')

print(tips.head())


#Bar Plot
sns.barplot(x='day', y = 'total_bill', data = tips)

plt.title("Average Total Bill by Day")

plt.show()
#Count plot
sns.countplot(x='day', data=tips, palette = 'viridis')

plt.title("Number of tips per Day")

plt.show()
#Box Plot
sns.boxplot(x='day', y='total_bill', data=tips)

plt.title("Total Bill by Day")

plt.show()
#histplot
sns.histplot(tips['total_bill'], bins = 20, kde = True)

plt.title("Distribution of Total Bills")

plt.show()
#kdeplot (Kernel Density Estimate)
sns.kdeplot(data=tips, x = 'total_bill')

plt.title("Kernel Density Estimate of Total Bills")

plt.show()
#scatterplot
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='smoker', style = 'time')

plt.title("Total Bill vs Tip Amount")

plt.show()
#lmplot (Linear Model Plot)
sns.lmplot(x='total_bill', y = 'tip', data = tips, hue ='smoker', col='sex')

plt.show()

numeric_tips = tips.select_dtypes(include=['number'])

correlation_matrix = numeric_tips.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

plt.show()

