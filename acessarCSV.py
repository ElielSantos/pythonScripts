 #codigo = input('')
    #codigo = codigo.upper()  # RESOLVE O PROBLEMA DE DIGITAR 'TR' e 'tr'...
    #if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
    #    print('')
    #    continue  # SE USUÁRIO DIGITAR ALGO INVÁLIDO, VOLTA PARA O INÍCIO DO WHILE

import pandas as pd

print('.............................CSV..........................')
print('..........................................................')

nome=[]
serial=[]
ID=0


# Especifica o caminho completo para o arquivo CSV
caminho_arquivo_csv = '/home/ticientifica/Downloads/planilha.csv'

# Tenta ler o arquivo CSV usando o pandas
try:
    df = pd.read_csv(caminho_arquivo_csv)
    # Faça o que desejar com o DataFrame, por exemplo, exiba as primeiras linhas
    print(df.head())
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")

def adicionar(codico):
    print('#')
    nome=input('nome :')
    id=input('id: ')
    serial={'codico' : codico,
            'nome' : nome,
            'id '  : id,
            'serial' : serial,}
    #listaFuncionarios.append(serial.copy())
