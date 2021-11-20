# bibliotecas importadas
import pandas as pd

# dados inseridos numa chave
d = {
    "Nome": ["Ana", "Flávio", "Jéssica", "Billy"],
    "Idade": [20, 35, 38, 45],
    "Altura": [1.66, 1.78, 1.69, 2.00],
    "Atividade Física": ["Corrida", "Musculação", "Natação", "Ciclismo"]
}

# transformação em um conjunto de dados
dados = pd.DataFrame(data=d)

# transformação dos conjuntos de dados em um arquivo no excel
dados.to_excel("dados.xlsx", index=False)