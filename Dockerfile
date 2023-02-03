# Usando uma imagem de python como base
FROM python:3.9-alpine

# Definindo o diretório de trabalho como /app
WORKDIR /app

# Instalando as dependências do mysql
RUN apk --update add build-base && apk add --update mariadb-dev && apk add --update mysql-dev

# Copiando os arquivos necessários para a imagem do Docker
COPY requirements.txt .

# Instalando as dependências do projeto
RUN pip install -r requirements.txt

# Copiando o resto dos arquivos da aplicação para a imagem do Docker
COPY . .

# Executando as configurações necessárias do banco de dados
RUN python manage.py makemigrations && python manage.py migrate

# Executando o servidor do Django
CMD python manage.py runserver 0.0.0.0:8000