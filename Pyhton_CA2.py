import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df=pd.read_csv("D:/Downloads/Current Daily Price of Various Commodities from Various Markets (Mandi).csv")
print(df.head())
print(df.info())

print(df.isnull().sum())

df.rename(columns={
    'Min_x0020_Price': 'Min_Price',
    'Max_x0020_Price': 'Max_Price',
    'Modal_x0020_Price': 'Modal_Price'
}, inplace=True)

print(df.columns)

print("\n\nObjective 1: To show how many commodities are present per market\n\n")

top_markets = df['Market'].value_counts().nlargest(10)
sb.barplot(x=top_markets.values, y=top_markets.index)
plt.title("Top 10 Markets by Number of Commodity Entries")
plt.xlabel("Number of Entries")
plt.ylabel("Market")
plt.show()

print("\n\nObjective 2:To identify the top commodities being traded\n\n")

top_commodities = df['Commodity'].value_counts().nlargest(10)
sb.barplot(x=top_commodities.values, y=top_commodities.index)
plt.title("Top 10 Most Common Commodities")
plt.xlabel("Frequency")
plt.ylabel("Commodity")
plt.show()

print("\n\nObjective 3:To plot price distribution for selected commodities\n\n")

selected = df[df['Commodity'].isin(['Onion', 'Potato', 'Tomato'])]  # example
sb.boxplot(x='Commodity', y='Modal_Price', data=selected)
plt.title("Price Variation of Selected Commodities")
plt.ylabel("Modal Price")
plt.show()

print("\n\nObjective 4:State-wise Commodity Availability\n\n")
state_counts = df['State'].value_counts()
sb.barplot(x=state_counts.values, y=state_counts.index)
plt.title("Number of Commodity Records by State")
plt.xlabel("Count")
plt.ylabel("State")
plt.show()

print("\n\nObjective 5:Price Correlation between Min, Modal and Max Prices\n\n")

price_data = df[['Min_Price', 'Modal_Price', 'Max_Price']]
correlation = price_data.corr()

plt.figure(figsize=(6, 4))
sb.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Price Types")
plt.show()


