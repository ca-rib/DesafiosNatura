# Importando copy e OS
import os
from shutil import copy

# 1 - Criar duas pastas ( Avon/Natura)
# Criação da pasta feita com função makedirs()
os.makedirs(r'C:/Users/332685/OneDrive - Natura Cosméticos/Área de Trabalho/Desafio/Natura')
os.makedirs(r'C:/Users/332685/OneDrive - Natura Cosméticos/Área de Trabalho/Desafio/Avon')

# 2 - Dentro da pasta Avon criar um arquivo avon00.txt
# 3 - Dentro deste arquivo colocar uma frase de música
# Flush usado para garantir que os dados armazenados em buffer sejam escritos imediatamente
arquivo = open(r'C:/Users/332685/OneDrive - Natura Cosméticos/Área de Trabalho/Desafio/Avon/avon00.txt', 'a')
arquivo.write("Meu escritório é na praia, eu tô sempre na área")
arquivo.flush()

# 4 - Fazer uma cópia, do arquivo, para a pasta Natura. No formato natura00.txt
# 5 - Fazer 100x (cópias) na pasta natura e na pasta avon
contador = 0
while contador < 100:
    origem = r'C:/Users/332685/OneDrive - Natura Cosméticos/Área de Trabalho/Desafio/Avon/avon00.txt'
    destino_natura = rf'C:/Users/332685/OneDrive - Natura Cosméticos/Área de Trabalho/Desafio/Natura/natura{contador:02d}.txt'
    destino_avon = rf'C:/Users/332685/OneDrive - Natura Cosméticos/Área de Trabalho/Desafio/Avon/avon{contador:02d}.txt'
    
# Copiar para a pasta Natura
    copy(origem, destino_natura)
    
# Copiar para a pasta Avon (exceto para a primeira cópia)
    if contador != 0:
        copy(origem, destino_avon)

# Acrescentar 1 ao contador
    contador += 1 

print('Foram feitas 100 cópias do arquivo da pasta Avon para pasta Natura e Avon')
