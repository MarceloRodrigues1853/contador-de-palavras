"""
Versão refatorada do contador de palavras usando orientação a objetos.
Exemplo de como a IA pode ajudar na refatoração de código.
"""

import re
from collections import Counter


class ContadorPalavras:
    """Classe para contar palavras em arquivos de texto."""

    def __init__(self, arquivo):
        """
        Inicializa o contador com um arquivo.
        
        Args:
            arquivo (str): Caminho para o arquivo de texto.
        """
        self.arquivo = arquivo
        self.texto = None
        self.palavras = []
        self.total_palavras = 0
        self.contador = None

    def ler_arquivo(self):
        """
        Lê o conteúdo do arquivo especificado.
        
        Raises:
            FileNotFoundError: Se o arquivo não existir.
        """
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                self.texto = f.read()
        except FileNotFoundError:
            raise FileNotFoundError("O arquivo especificado não existe.")

    def contar_palavras(self):
        """
        Separa o texto em palavras e conta o total.
        """
        if not self.texto:
            self.ler_arquivo()
        
        # Separe o conteúdo em palavras
        self.palavras = re.findall(r"\w+", self.texto.lower())
        self.total_palavras = len(self.palavras)
        
        # Cria contador de frequências
        self.contador = Counter(self.palavras)

    def obter_palavras_mais_frequentes(self, n=10):
        """
        Retorna as n palavras mais frequentes.
        
        Args:
            n (int): Número de palavras mais frequentes a retornar.
        
        Returns:
            list: Lista de tuplas (palavra, frequência).
        """
        if not self.contador:
            self.contar_palavras()
        
        return self.contador.most_common(n)

    def exibir_resultados(self, n=10):
        """
        Exibe o total de palavras e as mais frequentes.
        
        Args:
            n (int): Número de palavras mais frequentes a exibir.
        """
        if self.total_palavras == 0:
            self.contar_palavras()
        
        print(f"Total de palavras: {self.total_palavras}")
        
        mais_comuns = self.obter_palavras_mais_frequentes(n)
        
        print("\nPalavras mais frequentes:")
        for palavra, freq in mais_comuns:
            print(f"{palavra}: {freq}")


def main():
    """Função principal do programa."""
    arquivo = input("Digite o caminho para o arquivo de texto: ")
    
    try:
        contador = ContadorPalavras(arquivo)
        contador.exibir_resultados()
    except FileNotFoundError as e:
        print(str(e))
        exit(1)


if __name__ == "__main__":
    main()
