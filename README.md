# Contador de Palavras em Arquivos de Texto

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![License](https://img.shields.io/badge/License-Educacional-green.svg)
![Status](https://img.shields.io/badge/Status-Funcionando-success.svg)
![Pytest](https://img.shields.io/badge/Pytest-Tests%20Passing-brightgreen.svg)

Projeto Python para contar palavras em arquivos de texto.

> 💻 Este projeto foi desenvolvido na IDE **Cursor**, utilizando assistência de IA para desenvolvimento e debugging.

## 📋 Descrição

Este projeto conta palavras em arquivos de texto e mostra:
- O total de palavras no arquivo
- As 10 palavras mais frequentes e suas contagens

## 🚀 Como usar

### Pré-requisitos

- Python 3.12 ou superior
- Ambiente virtual (venv)

### Instalação

1. Clone ou baixe este projeto
2. Navegue até a pasta do projeto:
   ```bash
   cd contador_de_palavras
   ```

3. Ative o ambiente virtual:
   ```bash
   # No Windows
   venv\Scripts\activate
   
   # No Linux/Mac
   source venv/bin/activate
   ```

4. Instale as dependências (se necessário):
   ```bash
   pip install -r requirements.txt
   ```

### Execução

Execute o script:
```bash
python contador.py
```

Digite o caminho para o arquivo de texto quando solicitado.

**Exemplo:**
```
Digite o caminho para o arquivo de texto: texto_teste.txt
```

### Arquivo de Teste

Um arquivo de exemplo (`texto_teste.txt`) está incluído no projeto para testes.

## 📁 Estrutura do Projeto

```
contador_de_palavras/
├── contador.py          # Script principal
├── texto_teste.txt      # Arquivo de exemplo para testes
├── requirements.txt     # Dependências do projeto
├── .gitignore          # Arquivos ignorados pelo Git
├── README.md           # Este arquivo
└── venv/               # Ambiente virtual (não versionado)
```

## 🔧 Funcionalidades

- **Leitura de arquivo**: Lê arquivos de texto com codificação UTF-8
- **Contagem de palavras**: Usa expressões regulares (`re.findall`) para separar palavras
- **Frequência de palavras**: Usa `Counter` do módulo `collections` para contar frequências
- **Tratamento de erros**: Trata exceções quando o arquivo não é encontrado

## 📝 Sobre o Projeto

Este projeto foi criado seguindo as boas práticas de Python:
- Uso de `with open()` para leitura segura de arquivos
- Tratamento de exceções (`FileNotFoundError`)
- Uso de `Counter` para contagem de frequências
- Código limpo e legível

## 📝 Licença

Este é um projeto educacional.
