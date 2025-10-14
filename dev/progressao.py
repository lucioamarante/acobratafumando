import pandas as pd

# --- Parâmetros Definidos ---
valor_inicial_global = 1000.00
percentual_entrada = 0.02  # 2% em formato decimal
numero_dias = 30
nome_do_arquivo = 'progressao_linear.xlsx'

# --- Cálculos ---

# 1. Calcular o valor fixo da entrada (2% do valor inicial original)
valor_da_entrada_fixo = valor_inicial_global * percentual_entrada

# 2. Preparar uma lista para armazenar os dados de cada dia
dados_para_tabela = []

# 3. Iniciar o valor que será atualizado a cada dia
valor_do_dia = valor_inicial_global

# 4. Loop para simular os 30 dias
for dia in range(1, numero_dias + 1):
    # O valor inicial da linha atual é o valor com que o dia começou
    valor_inicial_da_linha = valor_do_dia
    
    # O valor final é o valor inicial do dia + a entrada fixa
    valor_final_da_linha = valor_inicial_da_linha + valor_da_entrada_fixo
    
    # Adicionar os dados do dia à nossa lista
    dados_para_tabela.append({
        'Dia': dia,
        'Valor Inicial': valor_inicial_da_linha,
        'Entradas (%)': f"{percentual_entrada*100}%",
        'Valor da Entrada': valor_da_entrada_fixo,
        'Valor Final': valor_final_da_linha
    })
    
    # Atualizar o valor para o início do próximo dia
    valor_do_dia = valor_final_da_linha

# 5. Criar a tabela (DataFrame) com a biblioteca Pandas
df = pd.DataFrame(dados_para_tabela)

# 6. Formatar colunas de moeda para melhor visualização
for coluna in ['Valor Inicial', 'Valor da Entrada', 'Valor Final']:
    df[coluna] = df[coluna].map('R$ {:,.2f}'.format)


# 7. Salvar a tabela em um arquivo Excel
# O argumento index=False remove a coluna de índice padrão do Pandas
df.to_excel(nome_do_arquivo, index=False)

print(f"Tabela salva com sucesso no arquivo '{nome_do_arquivo}'!")