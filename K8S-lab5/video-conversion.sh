#!/bin/bash

# Caminho do vídeo de entrada
INPUT_VIDEO="input-video.mp4"

# Caminho do vídeo de saída
OUTPUT_VIDEO="output-video.avi"

# Usar o FFmpeg para converter o vídeo
ffmpeg -i $INPUT_VIDEO $OUTPUT_VIDEO

# Exibir a lista de arquivos convertidos
ls -l
