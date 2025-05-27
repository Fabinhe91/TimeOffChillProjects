# Usar a imagem oficial do Ubuntu como base
FROM ubuntu:latest

# Instalar o FFmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Criar o diretório de trabalho
WORKDIR /usr/src/app

# Copiar o script de conversão para dentro do container
COPY video-conversion.sh .

# Copiar o vídeo de entrada para dentro do container
COPY input-video.mp4 .

# Dar permissão ao script
RUN chmod +x video-conversion.sh

# Comando para rodar o script
CMD ["./video-conversion.sh"]
