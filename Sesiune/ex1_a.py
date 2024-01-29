import pandas as pd

file_path = r'C:\Users\Tudor\Desktop\pmp-lab1\Sesiune\BostonHousing.csv'
df = pd.read_csv(file_path, usecols=['medv', 'rm', 'crim', 'indus'])

print(df.head())
