# --- Calculadora de Rendimento com Juros Compostos ---

try:
    # 1. ENTRADA DE DADOS
    valor_inicial = float(input("Digite o valor inicial (ex: 1000): R$ "))
    taxa_percentual = float(input("Digite a taxa de rendimento por período (ex: 5 para 5%): % "))
    periodo = int(input("Digite a quantidade de períodos (ex: 12 meses): "))

    # 2. CÁLCULO
    # A fórmula de juros compostos é: M = C * (1 + i)^t
    # Onde:
    # M = Montante final
    # C = Capital inicial (valor_inicial)
    # i = Taxa de juros em decimal (taxa_percentual / 100)
    # t = Tempo / Período

    # Convertendo a taxa percentual para decimal
    taxa_decimal = taxa_percentual / 100

    # Aplicando a fórmula
    valor_final = valor_inicial * (1 + taxa_decimal) ** periodo
    
    # Calculando o total de juros ganhos
    total_juros = valor_final - valor_inicial

    # 3. APRESENTAÇÃO DO RESULTADO
    print("\n--------------------------------")
    print("✨ RESULTADO DO INVESTIMENTO ✨")
    print(f"Valor Inicial: R$ {valor_inicial:,.2f}")
    print(f"Taxa de Juros: {taxa_percentual}% por período")
    print(f"Período: {periodo} períodos")
    print("--------------------------------")
    print(f"O valor final será de: R$ {valor_final:,.2f}")
    print(f"Total de juros ganhos: R$ {total_juros:,.2f}")
    print("--------------------------------")

except ValueError:
    print("\nErro: Por favor, digite apenas números válidos para os valores.")