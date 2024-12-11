#! /bin/bash

apt update 
apt install -y python3 && apt install -y python3-pip
new_path = "export PATH\"\$PATH:/usr/bin\""
echo "$new_path" >> ~/.bashrc
source ~/.bashrc
pip install pandas==2.2.3
pip install fastapi==0.115
pip install uvicorn==0.32

# 로그 폴더 생성
log_dir="logs"
mkdir -p "$log_dir"

# 현재 날짜-시간 형식으로 로그 파일 이름 생성
timestamp=$(date +"%Y%m%d_%H%M%S")
log_file="$log_dir/model_$timestamp.log"

# nohup 명령어에서 로그 파일 경로 수정
nohup python3 model_api.py --host 0.0.0.0 --port 8888 > "$log_file" &
echo "----- RUN model -----"