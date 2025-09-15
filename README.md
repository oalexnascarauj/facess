# Facess - Backend base

Estrutura inicial do projeto Django para controle de chamada (frequência) por reconhecimento facial.

## Requisitos

- Python 3.10+
- PostgreSQL (local ou via Docker)

## Instalação

1) Crie e ative um virtualenv (Windows PowerShell):

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Instale as dependências:

```
pip install -r requirements.txt
```

3) Configure variáveis de ambiente: copie `.env.example` para `.env` e ajuste se necessário.

4) Suba serviços opcionais via Docker Compose (Postgres/Redis/MinIO):

```
docker compose up -d
```

5) Inicialize o banco e rode o servidor:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse http://127.0.0.1:8000 para a página inicial.

## Notas

- DRF já está instalado e pronto para uso.
- Tailwind e Bootstrap são carregados via CDN nesta base. Em produção, gere assets estáticos.
- Channels, Celery, Redis e MinIO estão preparados para uso futuro (não habilitados nesta base).
