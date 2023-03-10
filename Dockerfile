# Imagem Python oficial como base
FROM python:3.9-alpine

# Diretório de trabalho
WORKDIR /app

# Copiando o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalando as dependências do Python
RUN pip install -r requirements.txt

# Copiando todo o conteúdo do diretório atual para o diretório de trabalho
COPY . .

# Copiando arquivo zoado
COPY ./models.py /usr/local/lib/python3.9/site-packages/django/contrib/auth/models.py

# Executando o comando para iniciar o servidor Django
CMD python manage.py runserver 0.0.0.0:8000