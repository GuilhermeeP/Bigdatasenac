import pandas as pd

### ASSIMETRIA ###

# Carregar o DataFrame
pedidos_df = pd.read_csv("../Aula04/vendas_pedidos.csv")
dados_valor_total = pedidos_df['valor_total']

# 1. Calcular Assimetria
assimetria = dados_valor_total.skew()
print(f"Assimetria dos Valores Totais: {assimetria:.4f}")

# 2. Relembrar Média e Mediana para contextualizar
media = dados_valor_total.mean()
mediana = dados_valor_total.median()
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")

# 3. Análise da Assimetria
if assimetria >= -0.5 and assimetria <= 0.5:
    analise_assimetria = "Simétrica (ou Quase Simétrica). Média e Mediana são próximas."
elif assimetria > 0.5:
    analise_assimetria = "Positiva. A cauda se estende para a direita (valores maiores). Média > Mediana."
else:
    analise_assimetria = "Negativa. A cauda se estende para a esquerda (valores menores). Média < Mediana."

print(f"\nConclusão da Assimetria: {analise_assimetria}")

### CURTOSE ###

# 1. Calcular Curtose
curtose_excesso = dados_valor_total.kurtosis()

# 2. Calcular a Curtose Real
curtose_real = curtose_excesso + 3
print(f"Curtose em Excesso (Pandas): {curtose_excesso:.4f}")
print(f"Curtose Real (Referência 3.0): {curtose_real:.4f}")

# 3. Análise da Curtose
if curtose_real >= 2.5 and curtose_real <= 3.5:
    analise_curtose = "Mesocúrtica. Distribuição próxima da normal (dados uniformes no entorno da média)."
elif curtose_real < 2.5:
    analise_curtose = "Platicúrtica. Dados mais dispersos em relação à média. Caudas finas e Outliers comuns."
else: # curtose_real > 3.5
    analise_curtose = "Leptocúrtica. Dados extremamente concentrados no centro e caudas pesadas. Outliers muito comuns."

print(f"\nConclusão da Curtose: {analise_curtose}")