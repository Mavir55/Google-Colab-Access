import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(8, 5))
sns.lineplot(x=df['dia'], y=df['venda'], marker='o', linestyle='-')
plt.xlabel('Dia')
plt.ylabel('Preço da Gasolina (R$)')
plt.title('Preço da Gasolina em São Paulo - Julho/2021')
plt.grid(True)

plt.savefig('gasolina.png')
plt.show()
