#! /bin/bash

pip install streamlit==1.39.0
echo "----- RUN demo -----"
streamlit run demo.py backend 8888 --server.address 0.0.0.0 --server.port 8080