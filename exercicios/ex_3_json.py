import json
import os
import pandas as pd


path_to_dir = os.path.dirname(__file__)
path_to_json_file = os.path.join(path_to_dir, "dados_json.json")

with open(path_to_json_file, "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

df = pd.DataFrame(json_data)

df_min = df[df['valor'] == df['valor'].min()]
df_max = df[df['valor'] == df['valor'].max()]
df_workdays = df[df['valor'] > 0]

min_value = df_min.iloc[0,1]
max_value = df_max.iloc[0,1]
avg_value = df_workdays['valor'].mean() # Media dos valores dos faturamentos diarios nos dias de trabalho
gt_avg_count = df_workdays[df_workdays['valor'] > avg_value].count()['dia'] # Numero de dias com faturamento diario superior a media mensal

print(f"\nO menor valor de faturamento do mes ({min_value}) pode ser visualizado na tabela abaixo:\n")
print(df_min)

print(f"\nO maior valor de faturamento do mes ({max_value}) pode ser visualizado na tabela abaixo:\n")
print(df_max)

print(f"\n{gt_avg_count} dias do mes tiveram valor do faturamento diario superior a media mensal\n")
