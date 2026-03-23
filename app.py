# Cálculo de Consumo de Energia Elétrica

print("--- Calculadora de Consumo de Energia ---")

# Entrada de dados
nome_aparelho = input("Digite o nome do aparelho (ex: Geladeira): ")
potencia = float(input(f"Digite a potência do(a) {nome_aparelho} em Watts (W): "))
horas_dia = float(input(f"Quantas horas por dia o(a) {nome_aparelho} fica ligado(a)? "))

# Processamento
# Fórmula: Consumo Mensal (kWh) = (Potência * Horas * 30 dias) / 1000
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo de custo (Opcional - R$ 0,75 por kWh)
custo_estimado = consumo_mensal * 0.75

# Saída de dados formatada
print("-" * 40)
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo mensal estimado: R$ {custo_estimado:.2f} (Base: R$ 0,75/kWh)")
print("-" * 40)
