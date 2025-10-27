🏫 API de Alunos

Uma aplicação web simples e estilizada para gerenciar alunos e suas notas, construída com FastAPI, Jinja2 e Uvicorn.

Permite:

Listar alunos com notas e status (aprovado/reprovado)

Cadastrar novos alunos via formulário web

⚡ Tecnologias utilizadas

Python 3

FastAPI

Uvicorn

Jinja2

HTML / CSS

🔧 Instalação

Clone o repositório:

git clone https://github.com/usuario/api-alunos.git
cd api-alunos


Crie um ambiente virtual (opcional):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Instale as dependências:

pip install fastapi uvicorn jinja2


Estrutura do projeto:

api-alunos/
├─ main.py
├─ templates/
│  ├─ alunos.html
│  └─ cadastro.html
├─ static/
│  └─ style.css

🏃 Como executar
python -m uvicorn main:app --reload


Acesse no navegador:

http://127.0.0.1:8000/

📋 Funcionalidades

Exibir lista de alunos com nome, nota e status

Cadastro de novos alunos via formulário

Redirecionamento automático após cadastro

Diferencia visualmente alunos aprovados e reprovados

Interface estilizada com cores, sombras e botões interativos

⚡ Endpoints
Método	Rota	Descrição
GET	/	Lista todos os alunos
GET	/cadastro	Exibe formulário de cadastro
POST	/cadastro	Salva novo aluno e redireciona
🎨 Templates HTML
1. alunos.html
<!-- código do seu alunos.html aqui -->

2. cadastro.html
<!-- código do seu cadastro.html aqui -->

🎨 CSS (static/style.css)
/* Seu CSS completo enviado */

🖼️ Visual (simulado)

Lista de alunos:

Linhas verdes: aprovados

Linhas vermelhas: reprovados

Hover azul claro

Formulário de cadastro:

Caixa branca com sombra

Botão interativo azul

Link “Voltar”

✨ Contribuição

Fork o projeto

Crie uma branch (git checkout -b minha-nova-funcionalidade)

Faça commit das alterações (git commit -m 'Adiciona nova funcionalidade')

Push para a branch (git push origin minha-nova-funcionalidade)

Abra um Pull Request

📄 Licença

Este projeto está licenciado sob a MIT License