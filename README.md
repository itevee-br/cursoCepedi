# Trabalho do Curso CEPEDI

---

abaixo segue um guia passo a passo de como instalar e usar localmente.

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/itevee-br/cursoCepedi.git
cd cursoCepedi/escola
```

---

### 2️⃣ Criar e Ativar Ambiente Virtual

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
---

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Aplicar Migrações do Banco de Dados

```bash
cd escola
python manage.py migrate
```

---

### 5️⃣ Criar Superusuário

```bash
python manage.py createsuperuser
```

O terminal irá solicitar:

- Username
- Email (opcional)
- Password
- Confirmação da senha

Após finalizar, o usuário administrador estará criado.

---

### 6️⃣ Executar o Servidor

```bash
python manage.py runserver
```

O sistema estará disponível em:

```
http://127.0.0.1:8000
```
## 📱 Screenshots do Projeto

### 1. 🔐 Primeiro Login
> Tela exibida no primeiro acesso ao sistema
<br>
<img src="https://raw.githubusercontent.com/itevee-br/cursoCepedi/refs/heads/master/escola/staticfiles/admin/img/primeiroLogin.jpeg" width="600">

### 2. 📝 Cadastro de Aluno
> Formulário para registro de novos alunos
<br>
<img src="https://raw.githubusercontent.com/itevee-br/cursoCepedi/refs/heads/master/escola/staticfiles/admin/img/cadastroAluno.jpeg" width="600">

### 3. 📱 Menu Logado
> Interface principal após o login do usuário
<br>
<img src="https://raw.githubusercontent.com/itevee-br/cursoCepedi/refs/heads/master/escola/staticfiles/admin/img/menuLogado.jpeg" width="600">

### 4. 👥 Alunos Cadastrados
> Visualização da lista de alunos já matriculados no sistema
<br>
<img src="https://raw.githubusercontent.com/itevee-br/cursoCepedi/refs/heads/master/escola/staticfiles/admin/img/alunosCadastrados.jpeg" width="600">

---

### 🔁 Para acessar novamente (segundo login em diante)
Depois que o projeto já está configurado, use estes comandos sempre que quiser rodar o servidor:
```bash
# 1. Navegue até a pasta do projeto
cd cursoCepedi

# 2. Ative o ambiente virtual
venv\Scripts\activate

# 3. Entre na pasta do projeto Django
cd escola

# 4. Inicie o servidor
python manage.py runserver
```

---

Para encerrar o servidor: Pressione CTRL + C no terminal onde ele está rodando.
Após desligar, pode sair do ambiente virtual com
```bash
deactivate
```
---
