import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/Tudor/Desktop/pmp-lab1/PMP-2023-main/Lab7/auto-mpg.csv'

df = pd.read_csv(file_path)

df = df.dropna(subset=['CP', 'mpg'])

plt.figure(figsize=(10, 6))
plt.scatter(df['CP'], df['mpg'], alpha=0.5)
plt.title('Relația dintre CP și mpg')
plt.xlabel('Cai putere (CP)')
plt.ylabel('Consum de carburant (mpg)')
plt.show()
