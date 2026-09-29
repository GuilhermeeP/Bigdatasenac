import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Biblioteca para visualização mais elaborada

# 1. Carregar os dados de produtos
produtos_df = pd.read_csv("../Aula03/vendas_produtos.csv")
dados_preco = produtos_df['preco']

# 2. Calcular Medidas
media_preco = dados_preco.mean()
mediana_preco = dados_preco.median()
std_preco = dados_preco.std(ddof=0) # Desvio padrão populacional

assimetria_preco = dados_preco.skew()
curtose_excesso_preco = dados_preco.kurtosis()
curtose_real_preco = curtose_excesso_preco + 3 # Para a nossa referência de 3.0

# 3. Painel de Resultados

print("-" * 50)
print("PAINEL: DISTRIBUIÇÃO DOS PREÇOS DOS PRODUTOS")
print("-" * 50)
print(f"Média do Preço: R$ {media_preco:.2f}")
print(f"Mediana do Preço: R$ {mediana_preco:.2f}")
print(f"Desvio Padrão: R$ {std_preco:.2f}")
print("-" * 50)
print(f"Assimetria: {assimetria_preco:.4f}")
# Interpretação da Assimetria
if assimetria_preco > 0.5:
    print(" -> Assimétrica Positiva (Cauda à Direita). Média > Mediana. Produtos mais caros 'puxam' a cauda.")
elif assimetria_preco < -0.5:
    print(" -> Assimétrica Negativa (Cauda à Esquerda). Média < Mediana. Produtos mais baratos 'puxam' a cauda.")
else:
    print(" -> Simétrica. Média ≈ Mediana. Distribuição equilibrada.")

print(f"Curtose (Real, Ref. 3.0): {curtose_real_preco:.4f}")
# Interpretação da Curtose
if curtose_real_preco > 3.5:
    print(" -> Leptocúrtica. Pico alto e caudas pesadas. Preços extremamente concentrados no centro (muitos outliers de preço).")
elif curtose_real_preco < 2.5:
    print(" -> Platicúrtica. Pico baixo. Preços mais dispersos em relação à média.")
else:
    print(" -> Mesocúrtica. Próximo à Normal. Distribuição uniforme dos preços.")
print("-" * 50)

# 4. Geração do Boxplot para visualização de Outliers
plt.figure(figsize=(8, 4))
sns.boxplot(x=dados_preco)
plt.title('Boxplot da Distribuição dos Preços dos Produtos')
plt.xlabel('Preço (R$)')
plt.show()

# 5. Geração do Histograma com KDE
plt.figure(figsize=(10, 6))
sns.histplot(dados_preco, kde=True, bins=30, color='skyblue', edgecolor='black', stat='density')

# Adicionar a Média e Mediana para referência
plt.axvline(media_preco, color='red', linestyle='--', label=f'Média: {media_preco:.2f}')
plt.axvline(mediana_preco, color='green', linestyle=':', label=f'Mediana: {mediana_preco:.2f}')

# Adicionar textos para Assimetria e Curtose (apenas para referência visual, não desenha uma linha específica)
plt.text(0.95, 0.95, f'Assimetria: {assimetria_preco:.2f}', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))
plt.text(0.95, 0.88, f'Curtose (Real): {curtose_real_preco:.2f}', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round,pad=0.5', fc='lightgreen', alpha=0.5))

plt.title('Distribuição dos Preços dos Produtos (Histograma com KDE)', fontsize=14)
plt.xlabel('Preço (R$)', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()