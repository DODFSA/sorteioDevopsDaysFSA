import csv
import random

def ler_nomes_do_csv(caminho_arquivo):
    nomes = []
    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            if linha:  # Ignora linhas vazias
                nomes.append(linha[0])
    return nomes

def sortear_nome(nomes):
    return random.choice(nomes)

# Caminho para o arquivo CSV
caminho_csv = 'nomes.csv'  

# Executando o sorteio
nomes = ler_nomes_do_csv(caminho_csv)
if nomes:
    nome_sorteado = sortear_nome(nomes)
    print(f'Nome sorteado: {nome_sorteado}')
else:
    print('A lista de nomes está vazia.')
