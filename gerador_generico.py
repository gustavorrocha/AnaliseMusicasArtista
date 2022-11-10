# Importa as funções do gerador de base de dados
from gerador_base.genericos.ImportarDados import criar_df_dados
from gerador_base.genericos.ImportarLetras import criar_df_letras
from gerador_base.genericos.LimparCSV import juntar_dataframes



ARTISTA = "Adele" # Nome do artista cujas letras serão obtidas


df_letras = criar_df_letras(ARTISTA) # Cria um DataFrame com as letras do artista escolhido
df_letras.to_csv(f"./Infos/Letras - {ARTISTA}.csv", sep=";", encoding="utf-8-sig") # Exporta o df em um csv

df_dados = criar_df_dados(ARTISTA, ["album", "single"]) # Cria um DataFrame com os dados das músicas do artista escolhido
df_dados.to_csv(f"./Infos/Dados - {ARTISTA}.csv", sep=";", encoding="utf-8-sig") # Exporta o df em um csv

df = juntar_dataframes(f"./Infos/Letras - {ARTISTA}.csv", f"./Infos/Dados - {ARTISTA}.csv")
df.to_csv(f"./Infos/{ARTISTA}.csv", sep=";", encoding="utf-8-sig") # Exporta o df em um csv