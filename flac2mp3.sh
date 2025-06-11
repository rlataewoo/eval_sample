#!/bin/bash

# 사용법: ./flac2mp3.sh <입력폴더> <출력폴더>

# 입력 인자 체크
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_folder> <output_folder>"
  exit 1
fi

INPUT_DIR="$1"
OUTPUT_DIR="$2"

# 출력 폴더 생성
mkdir -p "$OUTPUT_DIR"

# FLAC → MP3 변환  # VBR, qscale 2 (~190kbps)
for file in "$INPUT_DIR"/*.flac; do
  # 파일이 없을 경우 무시
  [ -e "$file" ] || continue

  filename=$(basename "$file" .flac)
#   ffmpeg -y -i "$file" -codec:a libmp3lame -b:a 320k "$OUTPUT_DIR/$filename.mp3"
  ffmpeg -y -i "$file" -codec:a libmp3lame -qscale:a 2 "$OUTPUT_DIR/$filename.mp3"
done

echo "✅ 변환 완료: $INPUT_DIR → $OUTPUT_DIR (CBR 320kbps)"