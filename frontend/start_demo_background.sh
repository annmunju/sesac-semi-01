#! /bin/bash

apt update 
apt install -y python3 && apt install -y python3-pip
new_path = "export PATH\"\$PATH:/usr/bin\""
echo "$new_path" >> ~/.bashrc
source ~/.bashrc
pip install streamlit==1.39.0

# 로그 폴더 생성
log_dir="logs"
mkdir -p "$log_dir"

# 현재 날짜-시간 형식으로 로그 파일 이름 생성
timestamp=$(date +"%Y%m%d_%H%M%S")
log_file="$log_dir/demo_$timestamp.log"

# nohup 명령어에서 로그 파일 경로 수정
echo "test@test.com" | nohup streamlit run demo.py 0.0.0.0 8888 --server.address 0.0.0.0 --server.port 8080 > "$log_file" &
echo "----- RUN demo -----"
