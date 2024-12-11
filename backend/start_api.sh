#! /bin/bash

echo "SeSAC0923!" | sudo apt update 
sudo apt install -y python3 && sudo apt install -y python3-pip
new_path = "export PATH\"\$PATH:/usr/bin\""
echo "$new_path" >> ~/.bashrc
source ~/.bashrc
pip install pandas==2.2
pip install fastapi==0.115
pip install uvicorn==0.32
# nohup python model_api.py --host ${hostIP} --port ${port} > model.log &
nohup python3 model_api.py --host 0.0.0.0 --port 8888 > model.log &
echo "----- RUN model -----"

