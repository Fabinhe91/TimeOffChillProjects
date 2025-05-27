# Usar uma imagem base com Python
FROM python:latest

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o código da aplicação
COPY app.py .

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["python", "app.py"]
