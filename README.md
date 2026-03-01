# Trabalho do Curso CEPEDI

### 1️⃣ Clonar o Repositório

```bash
git clone (link_do_repositorio)
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

---

### 🔁 Para acessar novamente (segundo login em diante)
Depois que o projeto já está configurado, use estes comandos sempre que quiser rodar o servidor:
```bash
# 1. Navegue até a pasta do projeto
cd cepedi-curso

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
