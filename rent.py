import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/kenya-housing/rent.csv")

df

df.head(10)

first_10_rows = df.head(10)

# Save the first 10 rows to a new CSV file
first_10_rows.to_csv("C:/Users/Admin/OneDrive/Desktop/kenya-housing/first_10_rows.csv", index=False)

first_10_rows

first_10_rows.drop_duplicates()

first_10_rows.fillna(0)

first_10_rows.to_csv("C:/Users/Admin/OneDrive/Desktop/kenya-housing/first_10_rows.csv", index=False)

first_10_rows

first_10_rows.columns

df['Price'] = df['Price'].str.replace('KSh ', '').str.replace(',', '').astype(float)
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price (KSh)')
plt.ylabel('Frequency')
plt.show()

plt.scatter(df['sq_mtrs'], df['Price'], color='green', alpha=0.6)
plt.title('Price vs Square Meters')
plt.xlabel('Square Meters')
plt.ylabel('Price (KSh)')
plt.grid(True)
plt.show()

plt.scatter(df['Bedrooms'], df['Price'], color='orange', alpha=0.6)
plt.title('Price vs Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price (KSh)')
plt.grid(True)
plt.show()

plt.scatter(df['Bathrooms'], df['Price'], color='purple', alpha=0.6)
plt.title('Price vs Bathrooms')
plt.xlabel('Number of Bathrooms')
plt.ylabel('Price (KSh)')
plt.grid(True)
plt.show()

plt.scatter(df['sq_mtrs'], df['Price'], s=df['Bedrooms']*10, alpha=0.5, color='red')
plt.title('Price vs Square Meters (Bubble Plot)')
plt.xlabel('Square Meters')
plt.ylabel('Price (KSh)')
plt.grid(True)
plt.show()

df[df['Bedrooms'] == 2]['Price'].plot(kind='hist', bins=10, alpha=0.5, color='blue', label='2 Bedrooms')
df[df['Bedrooms'] == 3]['Price'].plot(kind='hist', bins=10, alpha=0.5, color='green', label='3 Bedrooms')
df[df['Bedrooms'] == 4]['Price'].plot(kind='hist', bins=10, alpha=0.5, color='red', label='4 Bedrooms')
plt.title('Price Distribution by Bedrooms')
plt.xlabel('Price (KSh)')
plt.ylabel('Frequency')
plt.legend()
plt.show()




