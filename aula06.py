import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Continuando exatamente de onde paramos na aula passada (histograma), vamos calcular os quartis e verificar se a média está dentro da faixa interquartil (entre Q1 e Q3).

q1 = np.percentile(precos_array, 25)
q2 = np.percentile(precos_array, 50)
q3 = np.percentile(precos_array, 75)

print(f"\nPrimeiro Quartil (Q1): R$ {q1:.2f}")
print(f"Segundo Quartil (Mediana/Q2): R$ {q2:.2f}")
print(f"Terceiro Quartil (Q3): R$ {q3:.2f}")

if q1 <= media <= q3:
    print("\nA média está DENTRO da faixa interquartil (entre Q1 e Q3).")
else:
    print("\nA média está FORA da faixa interquartil (fora de Q1 e Q3).")

plt.axvline(x=q1, color='green', linestyle='--', label=f'Q1: R$ {q1:.2f}')
plt.axvline(x=q3, color='orange', linestyle='--', label=f'Q3: R$ {q3:.2f}')
plt.axvline(x=media, color='red', linestyle='-', label=f'Média: R$ {media:.2f}')
plt.axvline(x=mediana, color='purple', linestyle='-', label=f'Mediana: R$ {mediana:.2f}')
plt.legend()
plt.show()

###################################################

# Calcular Q1 e Q3
Q1 = np.percentile(precos_array, 25)
Q3 = np.percentile(precos_array, 75)

# Calcular IQR
IQR = Q3 - Q1

# Calcular Limites
limite_superior = Q3 + (1.5 * IQR)
limite_inferior = Q1 - (1.5 * IQR)

print(f"\n--- Limites de Outliers (Preços dos Produtos) ---")
print(f"Q1 (25%): R$ {Q1:.2f}")
print(f"Q3 (75%): R$ {Q3:.2f}")
print(f"IQR: R$ {IQR:.2f}")
print(f"Limite Superior (LS): R$ {limite_superior:.2f}")
print(f"Limite Inferior (LI): R$ {limite_inferior:.2f}")

# Identificação de Outliers Superiores e Inferiores
outliers_superiores = df_produtos[df_produtos['preco'] > limite_superior]
outliers_inferiores = df_produtos[df_produtos['preco'] < abs(limite_inferior)]

# Exibir Outliers Superiores Ordenados (Decrescente)
print(f"\n--- Outliers Superiores ({len(outliers_superiores)} produtos) ---")
print(outliers_superiores[['nome', 'preco']].sort_values(by='preco', ascending=False))

# Exibir Outliers Inferiores Ordenados (Crescente)
print(f"\n--- Outliers Inferiores ({len(outliers_inferiores)} produtos) ---")
print(outliers_inferiores[['nome', 'preco']].sort_values(by='preco', ascending=True))

# Garante que os DataFrames de outliers não estão vazios antes de plotar
if not outliers_inferiores.empty or not outliers_superiores.empty:
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6)) # 1 linha, 2 colunas
    
    # 1ª Posição: Outliers Inferiores (Crescente)
    axes[0].bar(outliers_inferiores['nome'], outliers_inferiores['preco'])
    axes[0].set_title('Outliers Inferiores (Preços Mais Baixos)')
    axes[0].set_ylabel('Preço (R$)')
    axes[0].tick_params(axis='x', rotation=45, labelsize=8)
    axes[0].grid(axis='y', linestyle='--')
    
    # 2ª Posição: Outliers Superiores (Decrescente)
    # Ordenamos novamente para garantir a visualização correta
    outliers_superiores_plot = outliers_superiores.sort_values(by='preco', ascending=False)
    axes[1].bar(outliers_superiores_plot['nome'], outliers_superiores_plot['preco'])
    axes[1].set_title('Outliers Superiores (Preços Mais Altos)')
    axes[1].set_ylabel('Preço (R$)')
    axes[1].tick_params(axis='x', rotation=45, labelsize=8)
    axes[1].grid(axis='y', linestyle='--')
    
    plt.tight_layout() # Ajusta automaticamente os parâmetros de subplot para dar preenchimento
    plt.show()

else:
    print("\nNão houve outliers superiores ou inferiores para plotar.")
    
######################

import pandas as pd

# 1: LEITURA SEM PERDAS
# Se o CSV está quebrado (como a linha do Lucas Ferrão com 6 colunas em vez de 5),
# nós lemos o arquivo linha por linha e corrigimos o erro de separador decimal.

linhas_corrigidas = []
with open('treinamento_alunos.csv', 'r', encoding='latin1') as file:
    for linha in file:
        partes = linha.strip().split(',')
        
        # Se a linha tem 6 partes, é o erro do '850,00'. Vamos unir a parte 4 e 5.
        if len(partes) == 6:
            # Junta o '850' com '00' usando um ponto
            nova_linha = partes[:3] + [f"{partes[3]}.{partes[4]}"] + [partes[5]]
            linhas_corrigidas.append(nova_linha)
        else:
            linhas_corrigidas.append(partes)

# Criamos o DataFrame a partir da lista corrigida
df = pd.DataFrame(linhas_corrigidas[1:], columns=linhas_corrigidas[0])

print(f"Total de linhas carregadas: {len(df)}")
print(df.head())

# 2: RENOMEAR COLUNAS
df.columns = ['id', 'nome', 'data_nasc', 'mensalidade', 'curso']

# 3: TRATAR ENCODING
# Corrigindo os nomes e cursos que vieram como \xc3\xa9
def fix_encoding(text):
    if pd.isna(text) or text == '': return text
    try:
        # Tenta decodificar o que foi lido como string literal
        return text.encode('latin-1').decode('utf-8')
    except:
        return text

df['nome'] = df['nome'].apply(fix_encoding).str.strip()
df['curso'] = df['curso'].apply(fix_encoding).str.strip()

# 4: LIMPEZA DE CARACTERES
# Em vez de converter direto, limpamos tudo que não é número ou ponto
df['mensalidade'] = (
    df['mensalidade']
    .str.replace('R$', '', regex=False)
    .str.replace('.', '', regex=False) # Remove ponto de milhar
    .str.replace(',', '.')             # Troca vírgula decimal por ponto
    .str.strip()
)

# 5: MUDANÇA DE TIPOS
# Mudamos para numérico. Onde não for possível, ele vira NaN (vazio), mas a LINHA FICA.
df['mensalidade'] = pd.to_numeric(df['mensalidade'], errors='coerce')
df['id'] = pd.to_numeric(df['id'], errors='coerce')

df['data_nasc'] = pd.to_datetime(df['data_nasc'], dayfirst=True, errors='coerce')

# 6: TRATAR VALORES NULOS
# Em vez de dropna(), preenchemos com valores padrão para manter a linha
df['nome'] = df['nome'].replace('', 'NOME NÃO INFORMADO')
df['data_nasc'] = df['data_nasc'].fillna('DATA INVÁLIDA') # Vira string para manter o aviso

# 7: ANALISAR COM DESCRIBE
print("\n--- RESUMO ESTATÍSTICO ---")
# Agora o describe mostrará o outlier de 999.999 mas a linha continua lá
print(df.describe(include='all'))

# 8: LIDAR COM DUPLICADAS
# Em vez de apagar, vamos criar uma coluna que avisa se a linha é repetida
df['is_duplicada'] = df.duplicated(keep=False)


print(df)