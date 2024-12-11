#! /bin/bash

# apt update 
# apt install -y python3 && apt install -y python3-pip
# new_path = "export PATH\"\$PATH:/usr/bin\""
# echo "$new_path" >> ~/.bashrc
# source ~/.bashrc
pip install streamlit==1.39.0

# 로그 폴더 생성
log_dir="logs"
mkdir -p "$log_dir"

echo "----- RUN demo -----"
streamlit run demo.py 0.0.0.0 8888 --server.address 0.0.0.0 --server.port 8080
