#! /bin/bash

# apt update 
# apt install -y python3 && apt install -y python3-pip
# new_path = "export PATH\"\$PATH:/usr/bin\""
# echo "$new_path" >> ~/.bashrc
# source ~/.bashrc
pip install pandas==2.2.3
pip install fastapi==0.115
pip install uvicorn==0.32

# 로그 폴더 생성
log_dir="logs"
mkdir -p "$log_dir"

echo "----- RUN model -----"
python3 model_api.py --host 0.0.0.0 --port 8888
