"""
Testes unitários para o contador de palavras.
"""
import unittest
import os
import tempfile
from collections import Counter
import re


def contar_palavras_arquivo(arquivo):
    """
    Função auxiliar para contar palavras em um arquivo.
    Extraída do código principal para facilitar testes.
    """
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
    
    palavras = re.findall(r"\w+", texto.lower())
    total_palavras = len(palavras)
    contador = Counter(palavras)
    mais_comuns = contador.most_common(10)
    
    return total_palavras, mais_comuns


class TestContadorPalavras(unittest.TestCase):
    """Testes para o contador de palavras."""
    
    def setUp(self):
        """Configuração antes de cada teste."""
        # Criar arquivo temporário para testes
        self.arquivo_teste = tempfile.NamedTemporaryFile(
            mode='w', 
            encoding='utf-8', 
            delete=False,
            suffix='.txt'
        )
        self.arquivo_teste.close()
    
    def tearDown(self):
        """Limpeza após cada teste."""
        if os.path.exists(self.arquivo_teste.name):
            os.unlink(self.arquivo_teste.name)
    
    def test_contar_palavras_basico(self):
        """Testa contagem básica de palavras."""
        conteudo = "Python é uma linguagem de programação."
        with open(self.arquivo_teste.name, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        total, _ = contar_palavras_arquivo(self.arquivo_teste.name)
        # Python, é, uma, linguagem, de, programação = 6 palavras
        self.assertEqual(total, 6)
    
    def test_contar_palavras_multiplas_linhas(self):
        """Testa contagem de palavras em múltiplas linhas."""
        conteudo = """Python é uma linguagem.
        Python é poderosa.
        Python é fácil."""
        with open(self.arquivo_teste.name, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        total, _ = contar_palavras_arquivo(self.arquivo_teste.name)
        # Python, é, uma, linguagem, Python, é, poderosa, Python, é, fácil = 10 palavras
        self.assertEqual(total, 10)
    
    def test_contar_palavras_com_pontuacao(self):
        """Testa que pontuação não é contada como palavra."""
        conteudo = "Python, JavaScript, e Java são linguagens!"
        with open(self.arquivo_teste.name, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        total, _ = contar_palavras_arquivo(self.arquivo_teste.name)
        # Python, JavaScript, e, Java, são, linguagens = 6 palavras
        self.assertEqual(total, 6)
    
    def test_palavras_mais_frequentes(self):
        """Testa a contagem de palavras mais frequentes."""
        conteudo = "Python Python Python Java Java"
        with open(self.arquivo_teste.name, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        total, mais_comuns = contar_palavras_arquivo(self.arquivo_teste.name)
        
        # Verifica se Python aparece primeiro (mais frequente)
        self.assertEqual(mais_comuns[0][0], "python")
        self.assertEqual(mais_comuns[0][1], 3)
        
        # Verifica se Java aparece em segundo
        self.assertEqual(mais_comuns[1][0], "java")
        self.assertEqual(mais_comuns[1][1], 2)
    
    def test_arquivo_vazio(self):
        """Testa comportamento com arquivo vazio."""
        with open(self.arquivo_teste.name, 'w', encoding='utf-8') as f:
            f.write("")
        
        total, mais_comuns = contar_palavras_arquivo(self.arquivo_teste.name)
        self.assertEqual(total, 0)
        self.assertEqual(len(mais_comuns), 0)
    
    def test_case_insensitive(self):
        """Testa que a contagem não diferencia maiúsculas/minúsculas."""
        conteudo = "Python PYTHON python"
        with open(self.arquivo_teste.name, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        _, mais_comuns = contar_palavras_arquivo(self.arquivo_teste.name)
        # Todas as variações devem ser contadas como "python"
        self.assertEqual(mais_comuns[0][0], "python")
        self.assertEqual(mais_comuns[0][1], 3)


if __name__ == "__main__":
    unittest.main()
