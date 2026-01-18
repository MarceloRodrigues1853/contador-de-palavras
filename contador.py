# Programa para contar palavras em um arquivo de texto

# 1. Peça ao usuário o caminho para um arquivo de texto.
# 2. Leia o conteúdo do arquivo.
# 3. Separe em palavras.
# 4. Conte o número total de palavras.
# 5. (Opcional) Exibe as 10 palavras mais frequentes e sua contagem.

import re
from collections import Counter

arquivo = input("Digite o caminho para o arquivo de texto: ")

try:

    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print("O arquivo especificado não existe.")
    exit(1)

# Separe o conteúdo em palavras
palavras = re.findall(r"\w+", texto.lower())

total_palavras = len(palavras)

print(f"Total de palavras: {total_palavras}")

# Contagem de frequências
contador = Counter(palavras)
mais_comuns = contador.most_common(10)

print("\nPalavras mais frequentes:")
for palavra, freq in mais_comuns:
    print(f"{palavra}: {freq}")
