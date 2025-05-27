# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os requisitos e o código para o container
COPY requirements.txt .
COPY app.py .

# Instalar dependências
RUN pip install -r requirements.txt

# Expor a porta que o Flask vai usar
EXPOSE 5000

# Comando para rodar o servidor Flask
CMD ["python", "app.py"]
