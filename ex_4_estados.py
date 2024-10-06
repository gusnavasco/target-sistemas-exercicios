faturamento_mensal = {
    "SP": 67_836.43,
    "RJ": 36_678.66,
    "MG": 29_229.88,
    "ES": 27_165.48,
    "Outros": 19_849.53,
}

percentual_de_representacao = {}

faturamento_total = sum(faturamento_mensal.values())

for estado, faturamento in faturamento_mensal.items():
    percentual_de_representacao[estado] = str(round(faturamento/faturamento_total * 100, 2)) + " %"

print(percentual_de_representacao)
