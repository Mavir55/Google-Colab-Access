
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("gasolina.csv")

plt.figure(figsize=(8,5))
sns.lineplot(x=df["dia"], y=df["venda"], marker="o", linestyle="-", color="b", label="Preço da gasolina")
plt.title("Preço da Gasolina em São Paulo (Julho/2021)", fontsize=14)
plt.xlabel("Dia", fontsize=12)
plt.ylabel("Preço (R$)", fontsize=12)
plt.xticks(df["dia"])
plt.legend()
plt.grid()
plt.savefig("gasolina.png")
