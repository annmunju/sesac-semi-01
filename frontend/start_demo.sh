#! /bin/bash

echo "SeSAC0923!" | sudo apt update 
sudo apt install -y python3 && sudo apt install -y python3-pip
new_path = "export PATH\"\$PATH:/usr/bin\""
echo "$new_path" >> ~/.bashrc
source ~/.bashrc
pip install streamlit==1.39.0
# nohup streamlit run demo.py ${back_host} ${back_port} --server.address ${front_host} --server.port ${front_port} > demo.log &
echo "test@test.com" | nohup streamlit run demo.py 0.0.0.0 8888 --server.address 0.0.0.0 --server.port 8500 > demo.log &
echo "----- RUN demo -----"

