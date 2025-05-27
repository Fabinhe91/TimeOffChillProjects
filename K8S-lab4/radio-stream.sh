#!/bin/bash

# URL da estação de rádio (exemplo)
RADIO_URL="https://www-majesticjukeboxradio-com.filesusr.com/html/83e446_2103bb071347aaa55f28531fbdee4617.html#"

# Arquivo de saída
OUTPUT_FILE="/usr/src/app/output.mp3"

# Usar FFmpeg para capturar a rádio e salvar o arquivo
ffmpeg -i $RADIO_URL -acodec libmp3lame -ab 128k -ar 44100 -f mp3 $OUTPUT_FILE
