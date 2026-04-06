# Game Suggestion App

Aplicação web de recomendação de jogos que consome a **API IGDB** (base de dados com mais de 500 mil jogos). Desenvolvida com arquitetura back-end em Python/Flask e front-end modular com Jinja2.

## Sobre o projeto

O usuário pesquisa jogos por nome e recebe sugestões com informações detalhadas vindas diretamente da API da IGDB (Twitch/Igdb). O back-end autentica com a API via OAuth2, realiza as requisições e entrega os dados formatados para o front-end.

## Funcionalidades

- Busca de jogos por nome consumindo a API IGDB em tempo real
- Autenticação OAuth2 com a API da Twitch (credencial da IGDB)
- Exibição de informações dos jogos: nome, capa, descrição e plataformas
- Arquitetura modular: separação entre rotas, lógica de negócio e templates
- Variáveis de ambiente com `python-dotenv` para proteção de credenciais

## Tecnologias

- **Back-end:** Python 3, Flask, igdb-api-v4, python-dotenv
- **Front-end:** HTML, CSS, Jinja2
- **API:** [IGDB API v4](https://api-docs.igdb.com/)
- **Autenticação:** OAuth2 (Twitch Developer)

## Como executar

### Pré-requisitos

Crie uma conta em [dev.twitch.tv](https://dev.twitch.tv) e registre um aplicativo para obter `CLIENT_ID` e `CLIENT_SECRET`.

```bash
# Clone o repositório
git clone https://github.com/LeonardoSoriano824/Sugest-o-de-Game.git
cd Sugest-o-de-Game

# Instale as dependências
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto com suas credenciais:

```env
CLIENT_ID=seu_client_id
CLIENT_SECRET=seu_client_secret
```

```bash
# Execute a aplicação
python run.py
```

Acesse `http://localhost:5000` no navegador.

## Estrutura

```
Sugest-o-de-Game/
├── app/                  # Módulo principal da aplicação
│   ├── __init__.py       # Inicialização do Flask
│   ├── routes.py         # Rotas e lógica de negócio
│   └── templates/        # Templates Jinja2
├── run.py                # Ponto de entrada da aplicação
├── requirements.txt      # Dependências
└── .gitignore
```

---

Desenvolvido por [Leonardo Soriano](https://github.com/LeonardoSoriano824)
