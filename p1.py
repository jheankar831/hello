import pandas as pd
data=pd.read_csv(r"D:\AI notes\Dataset\Dataset\auto-mpg.csv")
df=pd.DataFrame(data)

print(df)
Horsepower_mean = df['Horsepower'].mean()
print("\nMean horsepower:", Horsepower_mean)
Acceleration_std = df['Acceleration'].std()
print("\nStandard Deviation of acceleration:", Acceleration_std)
manufactured_by_year = df['Model Year'].value_counts().sort_index()
print("\nNumber of cars manufactured in each year:")
print(manufactured_by_year)
