# Galeria Doja Cat

Uma galeria de fotos dedicada à artista Doja Cat, desenvolvida com Django.

## Funcionalidades

- Visualização de fotos da Doja Cat
- Categorização por tipo (shows, tapete vermelho, bastidores, etc.)
- Interface responsiva e moderna
- Sistema de administração para gerenciar as fotos

## Tecnologias Utilizadas

- Python 3.12
- Django 5.2
- Pillow (para processamento de imagens)
- HTML5/CSS3

## Como Executar o Projeto

1. Clone o repositório
2. Crie um ambiente virtual: `python3 -m venv venv`
3. Ative o ambiente virtual: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute as migrações: `python manage.py migrate`
6. Crie um superusuário: `python manage.py createsuperuser`
7. Inicie o servidor: `python manage.py runserver`

## Estrutura do Projeto

- `galeria/`: Aplicativo principal
- `media/`: Arquivos de mídia (fotos)
- `static/`: Arquivos estáticos (CSS, JS, etc.)
- `templates/`: Templates HTML 