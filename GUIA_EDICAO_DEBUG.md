# Guia de Edição e Depuração no Cursor

Este guia explica como usar as ferramentas de edição e depuração configuradas no projeto, conforme a aula 3.2.

## 🔍 Depuração (Debug)

### Configuração
O arquivo `.vscode/launch.json` já está configurado com três opções:

1. **Python: Arquivo Atual** - Depura o arquivo atualmente aberto
2. **Python: Contador de Palavras** - Depura o `contador.py` diretamente
3. **Python: Pytest** - Depura testes usando pytest

### Como Usar

1. **Definir pontos de interrupção (breakpoints):**
   - Clique à esquerda do número da linha no editor
   - Um círculo vermelho aparecerá

2. **Iniciar depuração:**
   - Pressione `F5` ou
   - Vá em **Executar > Iniciar Depuração**
   - Escolha a configuração desejada

3. **Controles de depuração:**
   - **F5**: Continuar
   - **F10**: Passar por cima (Step Over)
   - **F11**: Entrar (Step Into)
   - **Shift+F11**: Sair (Step Out)
   - **Ctrl+Shift+F5**: Reiniciar

4. **Painéis disponíveis:**
   - **Variáveis**: Mostra variáveis locais
   - **Watch**: Monitora expressões específicas
   - **Call Stack**: Mostra a pilha de chamadas
   - **Console**: Permite avaliar expressões

### Dica da IA
Se encontrar um valor inesperado durante a depuração, você pode:
- Copiar o trecho de código
- Perguntar ao chat: "Por que essa variável poderia ser None neste ponto?"

## 🧪 Testes

### Executar Testes

**Usando unittest (padrão Python):**
```bash
python -m unittest test_contador.py -v
```

**Usando pytest (recomendado):**
```bash
pytest test_contador.py -v
```

**Depurar testes:**
- Defina breakpoints no arquivo de teste
- Selecione "Python: Pytest" na configuração de depuração
- Pressione F5

### Testes Disponíveis

O arquivo `test_contador.py` contém:
- ✅ Teste básico de contagem de palavras
- ✅ Teste com múltiplas linhas
- ✅ Teste com pontuação
- ✅ Teste de palavras mais frequentes
- ✅ Teste de arquivo vazio
- ✅ Teste case-insensitive

### Adicionar Novos Testes

Use a IA para criar novos testes:
- "Escreva um teste para a função contar_palavras garantindo que ela conte corretamente palavras com acentos"
- A IA irá gerar o código de teste automaticamente

## 🎨 Formatação e Linting

### Black (Formatador)
O projeto está configurado para usar **Black** como formatador.

**Formatar manualmente:**
```bash
black contador.py
```

**Formatar todo o projeto:**
```bash
black .
```

**Configuração automática:**
- A formatação ao salvar está habilitada em `.vscode/settings.json`
- O código será formatado automaticamente ao salvar

### Pylint (Linter)
O **Pylint** está configurado para verificar problemas no código.

**Ver problemas:**
- Os problemas aparecem na aba **Problemas** do Cursor
- Sublinhados vermelhos/amarelos indicam erros/avisos

**Executar manualmente:**
```bash
pylint contador.py
```

## 🔄 Refatoração com IA

### Exemplo: Converter para Classe

Já existe um exemplo de refatoração em `CONTADOR_REFATORADO.py` que mostra como transformar o código processual em uma classe.

**Para refatorar outros códigos:**
1. Selecione o código que deseja refatorar
2. Pergunte ao chat:
   - "Refatore este código em uma classe ContadorPalavras com métodos ler_arquivo e contar_palavras"
   - A IA gerará uma versão refatorada

### Dicas de Refatoração
- A IA pode ajudar a melhorar a estrutura do código
- Sempre revise e entenda o código gerado
- Teste após refatorar para garantir que funciona

## 📝 Impressões de Depuração (Print Debugging)

Às vezes é mais rápido usar `print()` temporariamente:

**Adicionar prints:**
```python
print(f"Debug: total_palavras = {total_palavras}")
```

**Remover prints de depuração:**
- Use `Ctrl+K` no Cursor
- Selecione os prints
- Peça: "Remover prints de depuração"
- A IA removerá automaticamente

## ⚡ Otimização

**Perguntar sobre otimização:**
- "Como posso otimizar a parte da contagem de palavras?"
- A IA pode sugerir melhorias no algoritmo

**Nota:** O uso de `Counter` do `collections` já é bastante otimizado para este tipo de operação.

## 🛠️ Configurações do Projeto

### Arquivos de Configuração

- **`.vscode/launch.json`**: Configurações de depuração
- **`.vscode/settings.json`**: Configurações do editor (formatação, linting)
- **`pyproject.toml`**: Configurações do Black e Pytest

### Comandos Úteis

```bash
# Ativar ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Executar testes
python -m unittest test_contador.py -v

# Formatar código
black contador.py

# Verificar código
pylint contador.py
```

## 📚 Boas Práticas

1. **Sempre entenda o código:** Mesmo que a IA gere, você deve entender o que está acontecendo
2. **Teste regularmente:** Execute testes após fazer mudanças
3. **Mantenha código limpo:** Use formatação automática e linting
4. **Use versionamento:** Commite mudanças frequentes
5. **Documente:** Comente código complexo

---

**Pronto!** Agora você tem todas as ferramentas configuradas para desenvolver Python no Cursor de forma profissional. 🚀
