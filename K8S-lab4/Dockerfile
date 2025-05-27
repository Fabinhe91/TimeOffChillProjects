# Usar uma imagem base oficial do Ubuntu
FROM ubuntu:latest

# Instalar o FFmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Criar um diretório para o script
WORKDIR /usr/src/app

# Copiar o script que vai rodar o FFmpeg
COPY radio-stream.sh .

# Dar permissão de execução ao script
RUN chmod +x radio-stream.sh

# Comando para rodar o script
CMD ["./radio-stream.sh"]