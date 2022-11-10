import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime


# Importando os módulos das funções criadas
import analisador.AnaliseArtista as AA
import analisador.AnaliseLetras as AL


# Importa os dados do csv
ARTISTA = "Adele"
df = pd.read_csv(f"./Infos/{ARTISTA}_Com_Premios.csv", sep=",", encoding="utf-8-sig", index_col = 0) 
df.set_index('album',inplace = True) # Transforma a coluna do nome do álbum em index
df["duracao"] = (pd.to_datetime(df["duracao"], format="%M:%S") - datetime(1900,1,1)).dt.total_seconds() # Converte a duração para segundos


#==================================================================================  
#GRUPO DE PERGUNTAS 1

# i Músicas mais ouvidas e músicas menos ouvidas por Álbum
print(AA.max_e_min_album(df, "popularidade"))

# ii Músicas mais longas e músicas mais curtas por Álbum
print(AA.max_e_min_album(df, "duracao"))

# iii Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]
print(AA.max_e_min_musicas(df, "popularidade"))

# iv Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]
print(AA.max_e_min_musicas(df, "duracao"))

# v albuns mais premiado
if ARTISTA == "Adele": # Deixa de responder esse pergunta caso outro artista for escolhido
    print(AA.albuns_mais_premiados(df, 3))

# vi Existe alguma relação entre a duração da música e sua popularidade?
AA.corr_com_tempo(df, "popularidade") 


 

#GRUPO DE PERGUNTAS 1 - VISUALIZAÇÃO 

# Visualização do máximo e mínimo de aspectos por álbum
AA.visualizacao_maxmin_album(df, "popularidade")

# Visualização do máximo e mínimo de aspectos em toda a discografia do artista
AA.visualizacao_maxmin_musicas(df, "popularidade")



#==================================================================================   
#GRUPO DE PERGUNTAS 2

df_sem_albumidx = df.reset_index()

# i Quais são as palavras mais comuns nos títulos dos Álbuns?
print(AL.palavras_comuns(df_sem_albumidx, "album", "./Imgs/album.png"))

# ii Quais são as palavras mais comuns nos títulos das músicas?
print(AL.palavras_comuns(df_sem_albumidx, "nome", "./Imgs/nome.png"))

# iii Quais são as palavras mais comuns nas letras das músicas, por Álbum?
print(AL.gerar_tag_cloud_por(df_sem_albumidx, "letra", "./Imgs/Albums", "album"))

# iv Quais são as palavras mais comuns nas letras das músicas, em toda a discografia?
print(AL.palavras_comuns(df_sem_albumidx, "letra", "./Imgs/letra.png"))

# v O título de um álbum é tema recorrente nas letras?
print(AL.proporção_comparativa(df_sem_albumidx, "letra", "album"))

# vi O título de uma música é tema recorrente nas letras?
print(AL.proporção_comparativa(df_sem_albumidx, "letra", "nome"))



#==================================================================================   
#GRUPO DE PERGUNTAS 3

# i Comparar duas colunas do data frame por meio de visualização grafica e de regressão linear
AA.plot(df, 'vivacidade' ,'popularidade')
AA.plot(df, 'dancabilidade' ,'energia')

# ii Comparar popularidade media do album com quantidade de premiações do album e suas musica
print(AA.comparar_popularidade_premios(df))

# iii Frenquencia do modo (maior ou menor) de toda a discografia, por album ou por musica.
print(AA.porcentagem_modo(df, "album"))
print(AA.porcentagem_modo(df, "musica"))
