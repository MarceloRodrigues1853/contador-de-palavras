# 🚀 Como Subir Projeto para o GitHub

Guia passo a passo super simples para subir seu projeto!

---

## 📋 Passo a Passo Completo

### **PASSO 1: Criar Repositório no GitHub** ⭐ (Faça isso PRIMEIRO!)

1. Acesse: https://github.com
2. Faça login na sua conta
3. Clique no botão **"New"** ou **"+"** (canto superior direito)
4. Selecione **"New repository"**
5. Preencha:
   - **Repository name**: ex: `contador-de-palavras` (ou outro nome que quiser)
   - **Description**: `Contador de palavras em arquivos de texto - Projeto Python`
   - Deixe **Público** ou **Privado** (você escolhe)
   - ⚠️ **NÃO marque** "Add a README file" (já temos um!)
   - ⚠️ **NÃO marque** "Add .gitignore" (já temos um!)
   - ⚠️ **NÃO marque** "Choose a license" (por enquanto)
6. Clique em **"Create repository"**
7. ⭐ **COPIE a URL** que aparece (algo como: `https://github.com/SEU_USUARIO/contador-de-palavras.git`)

---

### **PASSO 2: Abrir o Terminal** 💻

No Cursor:
- Pressione `` Ctrl+` `` (Ctrl + crase/acento grave) ou
- Menu: **Terminal > New Terminal**

**IMPORTANTE:** Certifique-se de estar na pasta do projeto:
```bash
cd contador_de_palavras
```

---

### **PASSO 3: Inicializar Git** (Se ainda não foi feito)

```bash
git init
```

Isso cria uma "caixa" Git vazia no seu projeto.

---

### **PASSO 4: Adicionar Arquivos** 📁

```bash
git add .
```

Isso adiciona TODOS os arquivos para serem enviados (o ponto `.` significa "tudo").

---

### **PASSO 5: Fazer o Primeiro Commit** 💾

```bash
git commit -m "Primeiro commit: contador de palavras funcionando"
```

Isso "salva" os arquivos no Git local (ainda não foi para o GitHub!).

---

### **PASSO 6: Conectar ao GitHub** 🔗

Substitua `SEU_USUARIO` e `NOME_DO_REPOSITORIO` pelos seus dados:

```bash
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

**OU se você copiou a URL do GitHub (PASSO 1), cole ela aqui!**

---

### **PASSO 7: Renomear Branch Principal** (Se necessário)

```bash
git branch -M main
```

Isso garante que a branch principal se chama `main`.

---

### **PASSO 8: Enviar para o GitHub** 🚀

```bash
git push -u origin main
```

**PRIMEIRA VEZ:** Pode pedir seu usuário e senha do GitHub. 
- **Usuário**: Seu nome de usuário do GitHub
- **Senha**: Use um **Personal Access Token** (veja abaixo como criar)

---

### **PASSO 9: Verificar** ✅

Acesse a URL do seu repositório no GitHub:
`https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO`

**SEUS ARQUIVOS DEVEM ESTAR LÁ! 🎉**

---

## 🔑 Como Criar Personal Access Token (Senha)

O GitHub não aceita mais senha normal, precisa de um "token":

### **Como Fazer:**

1. No GitHub, clique na sua **foto de perfil** (canto superior direito)
2. Vá em **Settings**
3. No menu lateral esquerdo, vá em **Developer settings**
4. Clique em **Personal access tokens** > **Tokens (classic)**
5. Clique em **Generate new token** > **Generate new token (classic)**
6. Dê um nome para o token (ex: `meu-projeto-python`)
7. Marque **expiration**: Escolha um prazo (ex: 90 dias)
8. Marque as permissões:
   - ✅ **repo** (full control of private repositories)
9. Clique em **Generate token**
10. ⚠️ **COPIE O TOKEN IMEDIATAMENTE** (você não verá mais!)
11. Use esse token como "senha" no `git push`

---

## 📝 Comandos Completos (Copy/Paste)

Se você já tem o repositório criado no GitHub, copie e cole estes comandos (um por vez):

```bash
# 1. Ir para a pasta do projeto
cd contador_de_palavras

# 2. Inicializar Git
git init

# 3. Adicionar todos os arquivos
git add .

# 4. Fazer commit
git commit -m "Primeiro commit: contador de palavras funcionando"

# 5. Conectar ao GitHub (SUBSTITUA pela URL do SEU repositório!)
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git

# 6. Renomear branch
git branch -M main

# 7. Enviar para o GitHub
git push -u origin main
```

---

## 🆘 Problemas Comuns

### **Erro: "repository not found"**
- Verifique se o nome do repositório está correto
- Verifique se você criou o repositório no GitHub primeiro (PASSO 1)
- Verifique se você está usando a URL correta com seu nome de usuário

### **Erro: "authentication failed"**
- Use Personal Access Token ao invés de senha
- Veja como criar token acima

### **Erro: "remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

### **Quer atualizar depois de mudar arquivos?**
```bash
git add .
git commit -m "Descrição das mudanças"
git push
```

---

## ✅ Checklist Final

Antes de fazer `git push`, confira:

- [ ] Repositório criado no GitHub (PASSO 1)
- [ ] Você está na pasta do projeto (`contador_de_palavras`)
- [ ] Arquivo `.gitignore` está funcionando (venv não será enviado)
- [ ] README.md está atualizado (opcional)
- [ ] Você copiou a URL do repositório GitHub
- [ ] Você tem um Personal Access Token (se for primeira vez)

---

## 🎯 Resumo Ultra Rápido

1. Criar repo no GitHub
2. `cd contador_de_palavras`
3. `git init`
4. `git add .`
5. `git commit -m "mensagem"`
6. `git remote add origin URL_DO_GITHUB`
7. `git push -u origin main`
8. PRONTO! 🎉

---

**Qualquer dúvida, consulte a documentação do GitHub!** 😊
